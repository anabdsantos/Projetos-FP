#2.1.1
def cria_intersecao(col,lin):
    '''
    cria intersecao: str x int → intersecao
    cria intersecao(col,lin) recebe um caracter e um inteiro correspondentes à coluna col e à linha lin 
    e devolve a intersecao correspondente. O construtor verifica a validade dos seus argumentos, gerando um ValueError com a
    mensagem 'cria_intersecao: argumentos invalidos' caso os seus argumentos nao sejam validos.
    '''
    if type(col)!=str or type(lin)!=int or len(col)!=1:
        raise ValueError('cria_intersecao: argumentos invalidos')
    if col>chr(83) or col<chr(65) or lin<1 or lin>19: #Dentro dos limites do tabuleiro
        raise ValueError('cria_intersecao: argumentos invalidos') 
    return (col,lin)

def obtem_col(i):
    '''
    obtem col: intersecao → str
    obtem col(i) devolve a coluna col da intersecao i.
    '''
    return i[0]

def obtem_lin(i):
    '''
    obtem lin: intersecao → int
    obtem lin(i) devolve a linha lin da intersecao i.
    '''
    return i[1]

def eh_intersecao(arg):
    '''
    eh intersecao: universal → booleano
    eh intersecao(arg) devolve True caso o seu argumento seja um TAD intersecao
    e False caso contrario.
    '''
    if type(arg)!=tuple: #Assumi que as interseçoes eram tuplos(imutáveis)
        return False
    c=obtem_col(arg)
    l=obtem_lin(arg)
    if type(c)!=str or type(l)!=int or len(c)!=1:
        return False
    if c>chr(83) or c<chr(65) or l>19 or l<1: #Verificação dos limites do tabuleiro
        return False
    return len(arg)==2

def intersecoes_iguais(i1,i2):
    '''
    intersecoes iguais: universal x universal → booleano
    intersecoes iguais(i1, i2) devolve True apenas se i1 e i2 sao intersecoes e sao
    iguais, e False caso contrario.
    '''
    return (obtem_col(i1)==obtem_col(i2) and obtem_lin(i1)==obtem_lin(i2)) 

def intersecao_para_str(i):
    '''
    intersecao para str : intersecao → str
    intersecao para str(i) devolve a cadeia de caracteres que representa o seu
    argumento'''
    return str(obtem_col(i))+str(obtem_lin(i))

def str_para_intersecao(s):
    '''
    str para intersecao: str → intersecao
    str para intersecao(s) devolve a intersecao representada pelo seu argumento.'''
    coluna=s[0]
    linha=int(s[1:]) #Se fosse s[1] apenas transformaria o primeiro dígito
    return cria_intersecao(coluna,linha)

def obtem_intersecoes_adjacentes(i,l): 
    '''
    obtem intersecoes adjacentes: intersecao x intersecao → tuplo
    obtem intersecoes adjacentes(i, l) devolve um tuplo com as intersecoes adjacentes
    a intersecao i de acordo com a ordem de leitura em que l corresponde a intersecao
    superior direita do tabuleiro de Go
    '''
    validas=()
    coluna=obtem_col(i)
    linha=obtem_lin(i)
    if linha>1: #Para garantir que o cria_intersecao não dá erro e todas se mantenham dentro dos limites do tabuleiro
        baixo=cria_intersecao(coluna,linha-1)
        if eh_intersecao_valida(cria_goban_vazio(obtem_lin(l)),baixo):
            validas+=(baixo,)
    if coluna>'A': #''
        esquerda=cria_intersecao(chr(ord(coluna)-1),linha)
        if eh_intersecao_valida(cria_goban_vazio(obtem_lin(l)),esquerda):
            validas+=(esquerda,)
    if coluna<'S': #''
        direita=cria_intersecao(chr(ord(coluna)+1),linha)
        if eh_intersecao_valida(cria_goban_vazio(obtem_lin(l)),direita):
            validas+=(direita,)
    if linha<19: #''
        cima=cria_intersecao(coluna,linha+1)
        if eh_intersecao_valida(cria_goban_vazio(obtem_lin(l)),cima):
            validas+=(cima,)
    return validas

def ordena_intersecoes(t):
    '''
    ordena intersecoes: tuplo → tuplo
    ordena intersecoes(t) devolve um tuplo de intersecoes com as mesmas intersecoes
    de t ordenadas de acordo com a ordem de leitura do tabuleiro de Go.
    '''
    return tuple(sorted(t,key=lambda x:(obtem_lin(x),obtem_col(x)))) 

#2.1.2
def cria_pedra_branca():
    '''
    cria pedra branca: {} → pedra
    cria pedra branca() devolve uma pedra pertencente ao jogador branco.
    '''
    return ('O')

def cria_pedra_preta():
    '''
    cria pedra preta: {} → pedra
    cria pedra preta() devolve uma pedra pertencente ao jogador preto.
    '''
    return ('X')

def cria_pedra_neutra():
    ''' 
    cria pedra neutra: {} → pedra
    cria pedra neutra() devolve uma pedra neutra.
    '''
    return ('.')

def eh_pedra(arg):
    '''
    eh pedra: universal → booleano
    eh pedra(arg) devolve True caso o seu argumento seja um TAD pedra e False
    caso contrario.
    '''
    return arg in (cria_pedra_branca(),cria_pedra_preta(),cria_pedra_neutra())

def eh_pedra_branca(arg):
    '''
    eh pedra branca: pedra → booleano
    eh pedra branca(p) devolve True caso a pedra p seja do jogador branco e False
    caso contrario.
    '''
    return arg==cria_pedra_branca()

def eh_pedra_preta(arg):
    '''
    eh pedra preta: pedra → booleano
    eh pedra preta(p) devolve True caso a pedra p seja do jogador preto e False
    caso contrario.
    '''
    return arg==cria_pedra_preta()

def pedras_iguais(p1,p2):
    ''' 
    pedras iguais: universal x universal → booleano
    pedras iguais(p1, p2) devolve True apenas se p1 e p2 sao pedras e sao iguais.
    '''
    return eh_pedra(p1) and eh_pedra(p2) and p1==p2 #Têm que ser pedras, não basta serem iguais

def pedra_para_str(p):
    '''
    pedra para str : pedra → str
    pedra para str(p) devolve a cadeia de caracteres que representa o jogador dono
    da pedra, isto e, 'O', 'X' ou '.' para pedras do jogador branco, preto ou neutra
    respetivamente.
    '''
    if eh_pedra_branca(p):
        return 'O'
    elif eh_pedra_preta(p):
        return 'X'
    elif not eh_pedra_jogador(p):
        return '.'
    
def eh_pedra_jogador(p):
    '''
    eh pedra jogador : pedra → booleano
    eh pedra jogador(p) devolve True caso a pedra p seja de um jogador e False caso
    contrario.
    '''
    return eh_pedra_preta(p) or eh_pedra_branca(p)

#2.1.3
def cria_goban_vazio(n):
    '''
    cria goban vazio: int → goban
    cria goban vazio(n) devolve um goban de tamanho nxn, sem intersecoes ocupadas. O construtor verifica a validade do argumento, gerando um ValueError
    com a mensagem 'cria_goban_vazio: argumento invalido' caso o seu
    argumento nao seja valido.
    '''
    if type(n)!=int or n not in(9,13,19):
        raise ValueError('cria_goban_vazio: argumento invalido')
    return [[cria_pedra_neutra()] * n for listinhas in range(n)] #Escolhi listas como representação dos gobans
    #N listas de n pedras neutras 

def cria_goban(n,ib,ip):
    '''cria goban: int x tuplo x tuplo → goban
    cria goban(n, ib, ip) devolve um goban de tamanho n x n, com as intersecoes
    do tuplo ib ocupadas por pedras brancas e as intersecoes do tuplo ip ocupadas por pedras pretas. 
    O construtor verifica a validade dos argumentos, gerando
    um ValueError com a mensagem 'cria_goban: argumentos invalidos'
    caso os seus argumentos nao sejam validos.
    '''
    if type(n)!=int or n not in(9,13,19) or type(ib)!=tuple or type(ip)!=tuple:
        raise ValueError('cria_goban: argumentos invalidos')
    goban = cria_goban_vazio(n)
    for intersecao in ib:
        if intersecao in ip: #Não podem existir peças brancas e peças preta na mesma interseção
            raise ValueError('cria_goban: argumentos invalidos') 
    if len(ib)!=len(set(ib)) or len(ip)!=len(set(ip)): #Não pode existir repetições de interseções dentro de cada tipo de pedra
        raise ValueError('cria_goban: argumentos invalidos') #set tira os repetidos
    for inter_ib in ib:
        if type(inter_ib)!=tuple: #Todos os elementos têm que ser tuplos
            raise ValueError('cria_goban: argumentos invalidos')
        if not eh_intersecao_valida(goban,inter_ib):
            raise ValueError('cria_goban: argumentos invalidos')
    for inter_ip in ip:
        if type(inter_ip)!=tuple: #''
            raise ValueError('cria_goban: argumentos invalidos')
        if not eh_intersecao_valida(goban,inter_ip):
            raise ValueError('cria_goban: argumentos invalidos')
    for intersecaoB in ib: 
        coloca_pedra(goban,intersecaoB,cria_pedra_branca())
    for intersecaoP in ip:
        coloca_pedra(goban,intersecaoP,cria_pedra_preta())
    return goban
   
def cria_copia_goban(t):
    '''
    cria copia goban: goban → goban
    cria copia goban(t) recebe um goban e devolve uma copia do goban
    '''
    comprimentoT=obtem_lin(obtem_ultima_intersecao(t))
    copia=cria_goban_vazio(comprimentoT)
    for coluna in range(comprimentoT): #Acrescentar todos as pedras existentes em t numa cópia
        for linha in range(comprimentoT):
            intersecao=cria_intersecao(chr(65+coluna),linha+1)
            coloca_pedra(copia,intersecao,obtem_pedra(t,intersecao)) #Acrescentar todos as pedras existentes em t numa cópia
    return copia

def obtem_ultima_intersecao(g):
    '''
    obtem ultima intersecao: goban → intersecao
    obtem ultima intersecao(g) devolve a intersecao que corresponde ao canto superior direito do goban g.
    '''
    coluna=chr(64+len(g)) #Dá-nos a letra correspondente à ultima coluna 
    linha=len(g) #Dá-nos o número correspondente à ultima linha
    return cria_intersecao(coluna,linha)

def obtem_pedra(g,i):
    '''
    obtem pedra: goban x intersecao → pedra
    obtem pedra(g, i) devolve a pedra na intersecao i do goban g. Se a posicao
    nao estiver ocupada, devolve uma pedra neutra.
    '''
    return g[ord(obtem_col(i))-65][obtem_lin(i)-1]
      
def obtem_cadeia(g,i):
    '''
    obtem cadeia: goban x intersecao → tuplo
    obtem cadeia(g, i) devolve o tuplo formado pelas intersecoes (em ordem de
    leitura) das pedras da cadeia que passa pela intersecao i. Se a posicao nao
    estiver ocupada, devolve a cadeia de posicoes livres.
    '''
    intersecao=0
    cadeia=(i,) #Tem que se incluir a própria interseção
    while intersecao<len(cadeia):
        intersecoes=obtem_intersecoes_adjacentes(cadeia[intersecao],obtem_ultima_intersecao(g))
        for h in range(len(intersecoes)): #Não há repetição na cadeia
            if intersecoes[h] not in cadeia and\
             pedras_iguais(obtem_pedra(g,i),obtem_pedra(g,intersecoes[h])): #Cadeias de pedras iguais
                cadeia+=(intersecoes[h],)
        intersecao+=1
    return ordena_intersecoes(cadeia)

def coloca_pedra(g,i,p):
   '''
   coloca pedra: goban x intersecao x pedra → goban
   coloca pedra(g, i, p) modifica destrutivamente o goban g colocando a pedra
   do jogador p na intersecao i, e devolve o proprio goban.
   '''
   coluna=ord(obtem_col(i))-ord('A')
   linha=obtem_lin(i)-1
   if eh_pedra_branca(p):
      g[coluna][linha]=cria_pedra_branca()
   elif eh_pedra_preta(p):
      g[coluna][linha]=cria_pedra_preta()
   else: #p==cria_pedra_neutra()
     g[coluna][linha]=cria_pedra_neutra()
   return g 

def remove_pedra(g,i):
    '''
    remove pedra: goban x intersecao → goban
    remove pedra(g, i) modifica destrutivamente o goban g removendo a pedra
    da intersecao i, e devolve o proprio goban.
    '''
    g[ord(obtem_col(i))-ord('A')][obtem_lin(i)-1]=cria_pedra_neutra()
    return g

def remove_cadeia(g,t):
    '''  
    remove cadeia: goban x tuplo → goban
    remove cadeia(g, t) modifica destrutivamente o goban g removendo as pedras
    nas intersecoes to tuplo t, e devolve o proprio goban.
    '''
    for intersecoes in t:
        g[ord(obtem_col(intersecoes))-ord('A')][obtem_lin(intersecoes)-1]=cria_pedra_neutra()
    return g

def eh_goban(arg):
    '''
    eh goban: universal → booleano
    eh goban(arg) devolve True caso o seu argumento seja um TAD goban e False
    caso contrario.
    '''
    if type(arg)!=list: #Escolhi listas como a represntação do meu goban
        return False
    if len(arg) not in(9,13,19):
        return False
    for listinhas in arg:
        if type(listinhas)!=list or len(listinhas)!=obtem_lin(obtem_ultima_intersecao(arg)):
            return False #Garante as n listas de n elementos 
        for elementos in listinhas:
            if not((eh_pedra(elementos) and not eh_pedra_jogador(elementos)) or
                    eh_pedra_preta(elementos) or 
                    eh_pedra_branca(elementos)):
                return False
    return True

def eh_intersecao_valida(g,i):
    '''
    eh intersecao valida: goban x intersecao → booleano
    eh intersecao valida(g, i) devolve True se i e uma intersecao valida dentro do
    goban g e False caso contrario.
    '''
    if not eh_intersecao(i):
        return False
    letras = [chr(65 + j) for j in range(obtem_lin(obtem_ultima_intersecao(g)))] #Letras correspondentes aos caminhos verticais
    if obtem_col(i) not in letras: #Tem que estar dentro dos limites do tabuleiro
        return False
    return obtem_lin(i) >= 1 and obtem_lin(i) <= obtem_lin(obtem_ultima_intersecao(g)) #''

def gobans_iguais(g1,g2):
    ''' 
    gobans iguais: universal x universal → booleano
    gobans iguais(g1, g2) devolve True apenas se g1 e g2 forem gobans e forem
    iguais.
    '''
    if len(g1)!=len(g2): #Têm que ter o mesmo comprimento
        return False
    for colunas in range(obtem_lin(obtem_ultima_intersecao(g1))):
        for linhas in range(obtem_lin(obtem_ultima_intersecao(g1))):
            if not pedras_iguais(obtem_pedra(g1,cria_intersecao(chr(65+colunas),linhas+1)),
                                 obtem_pedra(g2,cria_intersecao(chr(65+colunas),linhas+1))):
                return False
    return True

def goban_para_str(g):
    '''
    goban para str : goban → str
    goban para str(g) devolve a cadeia de caracteres que representa o goban como
    mostrado nos exemplos.
    '''
    letras=''
    cadeia_de_numeros=''
    for letra in range(obtem_lin(obtem_ultima_intersecao(g))):
        letras+=' '+str((chr(65+letra))) #Retorna as letras correspondentes ao território
    for elemento in range(obtem_lin(obtem_ultima_intersecao(g))-1,-1,-1): #Retorna os números dos caminhos horizontais de forma inversa
        ponto=''
        numero=elemento+1
        for letra in range(obtem_lin(obtem_ultima_intersecao(g))):
            if eh_pedra_branca(obtem_pedra(g,cria_intersecao(chr(65+letra),elemento+1))):
                ponto+='O '
            elif not eh_pedra_jogador(obtem_pedra(g,cria_intersecao(chr(65+letra),elemento+1))):
                ponto+='. '
            elif eh_pedra_preta(obtem_pedra(g,cria_intersecao(chr(65+letra),elemento+1))):
                ponto+='X '
        if numero<=9:
            cadeia_de_numeros+='\n '+str(numero)+" "+ponto+" "+str(numero)
        else: #A partir do numero 10 o território exige outro tipo de formatação
            cadeia_de_numeros+='\n'+str(numero)+" "+ponto+str(numero)
    cadeia="  "+letras+cadeia_de_numeros+'\n'+"  "+letras
    return cadeia

def obtem_territorios(g):
    '''
    obtem territorios: goban → tuplo
    obtem territorios(g) devolve o tuplo formado pelos tuplos com as intersecoes de
    cada territorio de g. A funcao devolve as intersecoes de cada territorio ordenadas
    em ordem de leitura do tabuleiro de Go, e os territorios ordenados em ordem de
    leitura da primeira intersecao do territorio.
    '''
    territorios=()
    comprimentoG=obtem_lin(obtem_ultima_intersecao(g))
    for letras in range(comprimentoG):
        for numeros in range(comprimentoG):
            intersecao=cria_intersecao(chr(65+letras),numeros+1)
            if not eh_pedra_jogador(obtem_pedra(g,intersecao)): #Territórios são constituídos apenas por peças neutras
                PertenceAoutraCadeia=False
                for cadeia in territorios:
                    if intersecao in cadeia:
                        PertenceAoutraCadeia=True
                        break #Garantir que não verificamos as interseções que já pertencem a alguma cadeia (+eficiente)
                if not PertenceAoutraCadeia:
                 cadeia=obtem_cadeia(g,intersecao)
                 if cadeia not in territorios: #Garantir que não há repetição de cadeias
                     territorios+=(cadeia,)
    return tuple(sorted(territorios, key=lambda t: (obtem_lin(t[0]), obtem_col(t[0])))) #Meter por ordem os territórios, através do primeiro elemento de cada um

def obtem_adjacentes_diferentes(g,t):
    '''
    obtem adjacentes diferentes: goban x tuplo → tuplo
    obtem adjacentes diferentes(g, t) devolve o tuplo ordenado formado pelas intersecoes
    adjacentes as intersecoes do tuplo t:
    (a) livres, se as intersecoes do tuplo t estao ocupadas por pedras de jogador;
    (b) ocupadas por pedras de jogador, se as intersecoes do tuplo t estao livres.
    '''
    tuplo=()
    for intersecao in t:
        adjacentes=obtem_intersecoes_adjacentes(intersecao,obtem_ultima_intersecao(g))
        for pedra in adjacentes:
            if eh_pedra_jogador(obtem_pedra(g,intersecao)) and not eh_pedra_jogador(obtem_pedra(g,pedra)):
                if pedra not in tuplo:
                    tuplo+=(pedra,) #a) liberdades
            elif not eh_pedra_jogador(obtem_pedra(g,intersecao)) and eh_pedra_jogador(obtem_pedra(g,pedra)):
                if pedra not in tuplo:
                    tuplo+=(pedra,) #b) fronteiras
    return ordena_intersecoes(tuplo)

def jogada(g,i,p):
    '''
    jogada: goban x intersecao x pedra → goban
    jogada(g, i, p) modifica destrutivamente o goban g colocando a pedra de jogador
    p na intersecao i e remove todas as pedras do jogador contrario pertencentes a
    cadeias adjacentes a i sem liberdades, devolvendo o proprio goban.
    '''
    coloca_pedra(g,i,p) 
    if eh_pedra_preta(p):
        OtherPlayer=cria_pedra_branca()
    elif eh_pedra_branca(p):
        OtherPlayer=cria_pedra_preta() 
    adjacentes=obtem_intersecoes_adjacentes(i,obtem_ultima_intersecao(g))
    for intersecoes in adjacentes:
        if pedras_iguais(obtem_pedra(g,intersecoes),OtherPlayer):
            cadeia=obtem_cadeia(g,intersecoes)
            if obtem_adjacentes_diferentes(g,cadeia)==(): 
                remove_cadeia(g,cadeia) #Tira todas as pedras do outro jogador que ficaram sem liberdades
    return g

def obtem_pedras_jogadores(g):
    '''
    obtem pedras jogadores: goban → tuplo
    obtem pedras jogadores(g) devolve um tuplo de dois inteiros que correspondem ao
    numero de intersecoes ocupadas por pedras do jogador branco e preto, respetivamente.
    '''
    contaP=0
    contaB=0
    for coluna in range(obtem_lin(obtem_ultima_intersecao(g))):
        for linha in range(obtem_lin(obtem_ultima_intersecao(g))):
            intersecao=cria_intersecao(chr(65+coluna),linha+1)
            if eh_pedra_branca(obtem_pedra(g,intersecao)):
                contaB+=1 #Por todas as pedras brancas conta-se mais um
            elif eh_pedra_preta(obtem_pedra(g,intersecao)):
                contaP+=1 #Por todas as pedras pretas conta-se mais um
    return (contaB,contaP)

#2.2
#2.2.1
def calcula_pontos(g):
    '''
    calcula pontos(g) e uma funcao auxiliar que recebe um goban e devolve o tuplo de dois
    inteiros com as pontuacoes dos jogadores branco e preto, respetivamente.
    '''
    pedrasB,pedrasP=obtem_pedras_jogadores(g)
    territorios=obtem_territorios(g)
    if g==cria_goban_vazio(obtem_lin(obtem_ultima_intersecao(g))):
        return(0,0) #No início de um jogo os dois jogadores têm sempre 0 pontos
    for territorio in territorios:
        fronteira=obtem_adjacentes_diferentes(g,territorio)
        if all(eh_pedra_branca(obtem_pedra(g,intersecao)) for intersecao in fronteira):
            pedrasB+=len(territorio) #Acrescenta ao numero de pedras já existentes, as interseções pertencentes ao seu território
        elif all(eh_pedra_preta(obtem_pedra(g,intersecao)) for intersecao in fronteira):
            pedrasP+=len(territorio) #''
    return (pedrasB,pedrasP)

#2.2.2
def eh_jogada_legal(g,i,p,l):
    
    '''eh jogada legal(g, i, p, l) e uma funcao auxiliar que recebe um goban g, uma intersecao
    i, uma pedra de jogador p e um outro goban l e devolve True se a jogada for legal ou
    False caso contrario, sem modificar g ou l.'''
    if not eh_intersecao_valida(g,i) or eh_pedra_jogador(obtem_pedra(g,i)): 
        return False
    newTabuleiro=cria_copia_goban(g)
    jogada(newTabuleiro,i,p)
    cadeia=obtem_cadeia(newTabuleiro,i)
    if obtem_adjacentes_diferentes(newTabuleiro,cadeia)==(): #Suicídio
        return False
    return not(gobans_iguais(newTabuleiro,l)) and not(gobans_iguais(newTabuleiro,g)) #Repetição

#2.2.3
def turno_jogador(g,p,l):
    '''
    turno jogador(g, p, l) e uma funcao auxiliar que recebe um goban g, uma pedra de
    jogador p e um outro goban l, e oferece ao jogador que joga com pedras p a opcao de
    passar ou de colocar uma pedra propria numa intersecao. Se o jogador passar, a funcao
    devolve False sem modificar os argumentos. Caso contrario, a funcao devolve True e
    modifica destrutivamente o tabuleiro g de acordo com a jogada realizada. A funcao deve
    apresentar a mensagem do exemplo a seguir, repetindo a mensagem ate que o jogador
    introduzir 'P' ou a representacao externa de uma intersecao do tabuleiro de Go que
    corresponda a uma jogada legal.
    '''
    simbolo=""
    if eh_pedra_preta(p):
        simbolo="[X]"
    elif eh_pedra_branca(p):
        simbolo="[O]" #o símbolo muda consoante o jogador
    turno=True
    while turno:
        msg=input("Escreva uma intersecao ou 'P' para passar {}:".format(simbolo))
        if msg=='P':
            return False
        else:
         try:
           str_para_intersecao(msg) #Se a interseção dada estiver fora dos limites o loop recomeça
           if eh_intersecao_valida(g,str_para_intersecao(msg)) and eh_jogada_legal(g,str_para_intersecao(msg),p,l):
            jogada(g,str_para_intersecao(msg),p)
            turno=False
            return True 
         except ValueError: #Se ocorrer erro o loop recomeça
            continue
        
#2.2.4  
def go(n,tb,tp):
    '''
    go(n, tb, tn) e a funcao principal que permite jogar um jogo completo do Go de dois
    jogadores. A funcao recebe um inteiro correspondente a dimensao do tabuleiro, e dois
    tuplos (potencialmente vazios) com a representacao externa das intersecoes ocupadas
    por pedras brancas (tb) e pretas (tp) inicialmente. O jogo termina quando os dois
    jogadores passam a vez de jogar consecutivamente. A funcao devolve True se o jogador
    com pedras brancas conseguir ganhar o jogo, ou False caso contrario. A funcao deve
    verificar a validade dos seus argumentos, gerando um ValueError com a mensagem
    'go: argumentos invalidos' caso os seus argumentos nao sejam validos.
    '''
    if type(n)!=int or n not in(9,13,19):
        raise ValueError('go: argumentos invalidos') 
    novoTb=()
    novoTp=()   
    for inter_tb in tb:
        if type(inter_tb)==str:
         try:
            str_para_intersecao(inter_tb)
         except ValueError:
            raise ValueError('go: argumentos invalidos') #Garante que as interseções dadas estão dentro dos limites
         novoTb+=(str_para_intersecao(inter_tb),) #Se não der erro transforma as strings em interseções
        else:
            novoTb+=(inter_tb,) 
    for inter_tp in tp:
        if type(inter_tp)==str:
         try:
            str_para_intersecao(inter_tp)
         except ValueError:
            raise ValueError('go: argumentos invalidos') #Garante que as interseções dadas estão dentro dos limites
         novoTp+=(str_para_intersecao(inter_tp),) #Se não der erro transforma as strings em interseções
        else:
            novoTb+=(inter_tp,)   
    try:
        eh_goban(cria_goban(n,novoTb,novoTp))
    except ValueError:
        raise ValueError('go: argumentos invalidos') #Garantir que as restantes condições do goban são verificadas
    tabuleiro=cria_goban(n,novoTb,novoTp)
    tabuleiroantigo=cria_copia_goban(tabuleiro)
    jogadorP=cria_pedra_preta()
    jogadorB=cria_pedra_branca()
    atual=jogadorP #o primeiro a jogar é o jogador das peças pretas
    fim=0
    while fim<2: 
        pontosB,pontosP=calcula_pontos(tabuleiro)
        print("Branco (O) tem {} pontos\nPreto (X) tem {} pontos\n{}".format(pontosB,pontosP,goban_para_str(tabuleiro)))
        if not turno_jogador(tabuleiro,atual,tabuleiroantigo): 
            fim+=1 #Quando os dois passarem, fim atinge 2 e o jogo acaba
        atual=jogadorP if atual==jogadorB else jogadorB #Vai mudando de jogador conforme forem jogando
    pontosB,pontosP=calcula_pontos(tabuleiro)
    print("Branco (O) tem {} pontos\nPreto (X) tem {} pontos\n{}".format(pontosB,pontosP,goban_para_str(tabuleiro)))
    return pontosB>=pontosP #Retorna True se o jogador branco ganhar ou se empatarem e False caso contrário
