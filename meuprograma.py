def pergunta_nome():
    global nome
    nome = input("Qual é o seu nome? ")
    print('O seu nome é "' + nome + '"')
    return nome

def pergunta_idade(ano_atual=2017):    
    # Perguntar em que ano você nasceu
    ano_informado = int(input("Em que ano você nasceu " + nome + "? "))
    # Substrair o ano atual do ano informado
    idade = ano_atual - ano_informado
    # Imprimir na tela a idade calculado    
    print("Você tem",idade,"anos.")