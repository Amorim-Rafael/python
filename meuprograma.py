import datetime

class Entrevistado():

    nome = ""
    ano_informado = 0
    idade = 0

    def pergunta_nome(self):
        self.nome = input("Qual é o seu nome? ")
        print('O seu nome é "' + self.nome + '"')
        return self.nome
    
    def pergunta_idade(self):  
        ano_atual = datetime.date.today().year  
        # Perguntar em que ano você nasceu
        self.ano_informado = int(input("Em que ano você nasceu " + self.nome + "? "))
        # Substrair o ano atual do ano informado
        self.idade = ano_atual - self.ano_informado
        # Imprimir na tela a idade calculado    
        print("Você tem",self.idade,"anos.")
        #return (self.ano_informado, self.idade) #Tuple
    
    def __str__(self):
        return "{}/{}".format(self.nome, self.idade)

    def __repr__(self):
        return "input()={} input()=int({})".format(self.nome, self.idade)