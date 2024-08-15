def eh_territorio(arg):
    '''
    eh_territorio: universal -> booleano
    eh territorio(arg) recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a um territorio e False
    caso contrario, sem nunca gerar erros.
    '''
    if not isinstance(arg,tuple) or arg==(): #Como um território contem no mínimo um caminho horizontal o tuplo não pode ser vazio.
        return False
    if len(arg)>26 or len(arg)<1: #De A a Z 
        return False
    for i in range(len(arg)):
        if not isinstance(arg[i],tuple): #Como um território contem no mínimo um caminho vertical arg[i] tem que ser um tuplo
            return False
        comprimento=len(arg[0])
        if comprimento>99 or comprimento<1: #De 1 a 99
            return False
        if len(arg[i])!=comprimento: #Têm que todos o mesmo comprimento
            return False
        for g in arg[i]:
            if not(type(g)==(int) and (g==0 or g==1)): 
                return False
    return True

def obtem_ultima_intersecao(t):
   '''
   obtem ultima intersecao: territorio -> intersecao
   obtem ultima intersecao(t) recebe um territorio e devolve a intersecao do extremo superior direito do territorio.
   '''
   intersecao=()
   for tuplo in range(len(t)):
      if t[tuplo]==t[-1]: #Queremos obter o último tuplo
       vertical=chr(65+tuplo)
       for elemento in range(len(t[tuplo])):
          if t[tuplo][elemento]==t[tuplo][-1]: #Queremos obter o último elemento do último tuplo
            horizontal=(elemento+1)
       intersecao=(vertical,horizontal,) 
   return intersecao

def eh_intersecao(arg):
    ''' 
    eh intersecao: universal → booleano 
    eh intersecao(arg) recebe um argumento de qualquer tipo e devolve True se o seu argumento corresponde a uma intersecao 
    e False caso contrario, sem nunca gerar erros.
    '''
    if not isinstance(arg,tuple) or len(arg)!=2:
        return False
    if not isinstance(arg[0],str): 
        return False
    if arg[0]>chr(90) or arg[0]<chr(65): #De 'A' a 'Z'
        return False
    if len(arg[0])!=1: #Para não ser possível aceitar elementos como 'AA' por exemplo.
        return False
    if not (type(arg[1])==(int)): 
        return False    
    if (arg[1]<1 or arg[1]>99): #De 1 a 99
     return False
    return True

def eh_intersecao_valida(t, i):
    '''
    eh intersecao valida: territorio x intersecao -> booleano
    eh intersecao valida(t, i) recebe um territorio e uma intersecao, e devolve True se a
    intersecao corresponde a uma intersecao do territorio, e False caso contrario.
    '''
    if not eh_territorio(t) or not eh_intersecao(i): 
        return False
    letras = [chr(65 + g) for g in range(len(t))] #Letras correspondentes aos caminhos verticais
    if i[0] not in letras:  
        return False
    numero = len(t[0]) #Número de caminhos horizontais
    if i[1] < 1 or i[1] > numero:
        return False
    return True

def eh_intersecao_livre(t,i):
   '''
   eh intersecao livre: territorio x intersecao → booleano
   eh intersecao livre(t, i) recebe um territorio e uma intersecao do territorio, e devolve
   True se a intersecao corresponde a uma intersecao livre (nao ocupada por montanhas)
   dentro do territorio e False caso contrario.
   '''
   if eh_intersecao_valida(t,i):
    letra_correspondente=(ord(i[0])-65) #Ao código da letra da interseção retiramos o código da letra A. (Obtemos o número correspondente a i[0])
    if t[letra_correspondente][(i[1]-1)]!=0:
      return False
    return True

def obtem_intersecoes_adjacentes(t,i):  
    '''
    obtem intersecoes adjacentes: territorio x intersecao → tuplo
    obtem intersecoes adjacentes(t, i) recebe um territorio e uma intersecao do territorio, e
    devolve o tuplo formado pelas intersecoes validas adjacentes da intersecao em ordem de
    leitura de um territorio.
    ''' 
    intersecoes=()
    debaixo=(i[1]-1)
    esquerda=((chr(ord(i[0])-1)))
    direita=((chr(ord(i[0])+1)))
    cima=(i[1]+1)
    #Todas as interseções têm que estar dentro dos limites do território
    if debaixo>0: 
        intersecoes+=((i[0],debaixo),)
    if esquerda>='A':
        intersecoes+=((esquerda,i[1]),)
    if direita<=chr(65+(len(t)-1)): 
        intersecoes+=((direita,i[1]),)
    if cima<=len(t[0]):
        intersecoes+=((i[0],cima),)
    return intersecoes 

def ordena_intersecoes(tup):
    '''
    ordena intersecoes: tuplo → tuplo
    ordena intersecoes(tup) recebe um tuplo de intersecoes (potencialmente vazio) e devolve
    um tuplo contendo as mesmas intersecoes ordenadas de acordo com a ordem de leitura
    do territorio.
    '''
    lista=list(tup) #transformar numa lista porque tuplos são imutáveis
    #Usar o bubllesort, duas vezes. Uma para os números e outra para as letras
    for verticais in range(len(lista)):
        for horizontais in range(len(lista)-1-verticais): #len(lista)-1 permite usar "horizontais+1" 
            if lista[horizontais][1]>lista[horizontais+1][1]:
                lista[horizontais],lista[horizontais+1]=lista[horizontais+1],lista[horizontais]
    for verticais in range(len(lista)):
        for horizontais in range(len(lista)-1-verticais):
            if lista[horizontais][0]>lista[horizontais+1][0] and lista[horizontais][1]==lista[horizontais+1][1]:
                    lista[horizontais],lista[horizontais+1]=lista[horizontais+1],lista[horizontais] 
    return tuple(lista)

def territorio_para_str(t):
    '''
    territorio para str: territorio → cad. carateres 
    territorio para str(t) recebe um territorio e devolve a cadeia de caracteres que o representa (a representacao externa ou representacao “para os nossos olhos”).
    Se o argumento dado for invalido, a funcao deve gerar um erro com a mensagem 'territorio_para_str: argumento invalido'.
    '''
    letras=''
    cadeia_de_numeros=''
    if not eh_territorio(t):
        raise ValueError('territorio_para_str: argumento invalido')
    for letra in range(len(t)):
        letras+=' '+str((chr(65+letra))) #Retorna as letras correspondentes ao território
    for elemento in range(len(t[0])-1,-1,-1): #Retorna os números dos caminhos horizontais de forma inversa
        ponto=''
        numero=elemento+1
        for letra in range(len(t)):
            if t[letra][elemento]==1:
                ponto+='X '
            elif t[letra][elemento]==0:
                ponto+='. '
        if numero<=9:
            cadeia_de_numeros+='\n '+str(numero)+" "+ponto+" "+str(numero)
        else: #A partir do numero 10 o território exige outro tipo de formatação
            cadeia_de_numeros+='\n'+str(numero)+" "+ponto+str(numero)
    cadeia="  "+letras+cadeia_de_numeros+'\n'+"  "+letras
    return cadeia

def obtem_cadeia(t,i):
    '''
    obtem cadeia: territorio x intersecao → tuplo 
    obtem cadeia(t,i) recebe um territorio e uma intersecao do territorio (ocupada por uma
    montanha ou livre), e devolve o tuplo formado por todas as intersecoes que estao conetadas a essa intersecao ordenadas (incluida si propria) de acordo com a ordem de leitura
    de um territorio.  
    Se algum dos argumentos dado for invalido, a funcao deve gerar um erro com a mensagem 'obtem_cadeia: argumentos invalidos'.
    '''
    if not eh_intersecao_valida(t,i):
        raise ValueError('obtem_cadeia: argumentos invalidos')
    intersecao=0
    cadeia=(i,)
    while intersecao<len(cadeia):
        intersecoes=obtem_intersecoes_adjacentes(t,cadeia[intersecao])
        for h in range(len(intersecoes)): #Garantir que as intersecoes não se repetem na cadeia e que são iguais(ou montanhas ou livres)
            if intersecoes[h] not in cadeia and eh_intersecao_livre(t,i)==eh_intersecao_livre(t,intersecoes[h]):
                cadeia+=(intersecoes[h],)
        intersecao+=1
    return ordena_intersecoes(cadeia) 

def obtem_vale(t,i):
    '''
    obtem vale: territorio x intersecao → tuplo
    obtem vale(t,i) recebe um territorio e uma intersecao do territorio ocupada por uma montanha,
    e devolve o tuplo (potencialmente vazio) formado por todas as intersecoes que formam parte do vale da montanha 
    da intersecao fornecida como argumento ordenadas de acordo a ordem de leitura de um territorio. 
    Se algum dos argumentos dado for invalido, a funcao deve gerar um erro com a mensagem 'obtem_vale: argumentos invalidos'.
    '''
    if not(eh_intersecao_valida(t,i)) or eh_intersecao_livre(t,i): #(i) tem que ser uma montanha
        raise ValueError('obtem_vale: argumentos invalidos')
    vale=()
    cadeia=obtem_cadeia(t,i)
    for intersecao in cadeia:
        intersecoes=obtem_intersecoes_adjacentes(t,intersecao)
        for intersecao2 in intersecoes: #Para garantir que os vales não se repetem...
            if eh_intersecao_livre(t,intersecao2) and intersecao2 not in vale: #E um vale é obrigatoriamente uma intersecao livre
                vale+=(intersecao2,)

    return ordena_intersecoes(vale)

def verifica_conexao(t,i1,i2):
    '''
    verifica conexao: territorio x intersecao x intersecao → booleano
    verifica conexao(t,i1,i2) recebe um territorio e duas intersecoes do territorio e devolve
    True se as duas intersecoes estao conetadas e False caso contrario. 
    Se algum dos argumentos dado for invalido, a funcao deve gerar um erro com a mensagem 'verifica_conexao: argumentos invalidos'.
    '''
    if not (eh_territorio(t) and eh_intersecao_valida(t,i1) and eh_intersecao_valida(t,i2)):
        raise ValueError('verifica_conexao: argumentos invalidos')
    verificacao=obtem_cadeia(t,i1) #Para estarem conectadas têm que pertencer à mesma cadeia
    if i2 not in verificacao:
        return False
    return True

def calcula_numero_montanhas(t):
    '''
    calcula numero montanhas: territorio → int
    calcula numero montanhas(t) recebe um territorio e devolve o numero de intersecoes
    ocupadas por montanhas no territorio. 
    Se o argumento dado for invalido, a funcao deve gerar um erro com a mensagem 'calcula_numero_montanhas: argumento invalido'.
    '''
    if not eh_territorio(t):
        raise ValueError('calcula_numero_montanhas: argumento invalido')
    conta=0
    for vertical in range(len(t)):
        for horizontal in range(len(t[0])): #Verificação de todas as interseções do território
            if t[vertical][horizontal]==1: #Verificar se são montanhas
                conta+=1
    return conta

def calcula_numero_cadeias_montanhas(t):
    '''
    calcula numero cadeias montanhas: territorio → int
    calcula numero cadeias montanhas(t) recebe um territorio e devolve o numero de cadeias
    de montanhas contidas no territorio. 
    Se o argumento dado for invalido, a funcao deve gerar um erro com a mensagem 'calcula_numero_cadeias_montanhas: argumento invalido'.
    '''
    if not eh_territorio(t):
        raise ValueError('calcula_numero_cadeias_montanhas: argumento invalido')
    num_cadeias=()
    conta=0
    for verticais in range(len(t)):
        for horizontais in range(len(t[0])):
            if t[verticais][horizontais]==1: 
                cadeias=obtem_cadeia(t,(chr(65+verticais),horizontais+1))
                if cadeias not in num_cadeias:
                        num_cadeias+=(cadeias,) #Terá todas as cadeias de montanhas que existem no território
    return len(num_cadeias) #Conta os elementos(cadeias) do tuplo 

def calcula_tamanho_vales(t):
    '''
    calcula tamanho vales: territorio → int 
    calcula tamanho vales(t) recebe um territorio e devolve o numero total de intersecoes
    diferentes que formam todos os vales do territorio.
    Se o argumento dado for invalido, a funcao deve gerar um erro com a mensagem 'calcula_tamanho_vales: argumento invalido'.
    '''
    if not eh_territorio(t):
        raise ValueError('calcula_tamanho_vales: argumento invalido')
    tamanho_vales=()
    for verticais in range(len(t)):
        for horizontais in range(len(t[0])): 
            intersecao=(chr(65+verticais),horizontais+1) #Dá-nos todas as interseções existentes em t
            if eh_intersecao_valida(t,intersecao) and not(eh_intersecao_livre(t,intersecao)):
                vales=obtem_vale(t,intersecao)
                for vale2 in vales:
                    if vale2 not in tamanho_vales:
                        tamanho_vales+=(vale2,) #Terá todas os vales existentes
    return len(tamanho_vales)

