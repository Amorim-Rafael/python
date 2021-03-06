import datetime

class Entrevistado():

    nome = ""
    ano_informado = 0
    idade = 0

    def pergunta_nome(self):
        nome_digitado = False
        while nome_digitado == False:
            self.nome = input("Qual é o seu nome? (digite 'parar' para parar) ")
            if self.nome:
                nome_digitado = True
                if self.nome.lower() != 'parar':
                    print('O seu nome é "' + self.nome + '"')
        
        # title() deixa a primeira letra maiuscula e o restante minuscula
        self.nome = self.nome.title()                    
        
        return self.nome
    
    def pergunta_idade(self):  
        ano_atual = datetime.date.today().year  
        ano_digitado = False

        while ano_digitado == False:
            try:
                # Perguntar em que ano você nasceu
                self.ano_informado = int(input("Em que ano você nasceu " + self.nome + "? "))
                ano_digitado = True
            except:
                continue
            else:
                if self.ano_informado >= 1900 and self.ano_informado <= ano_atual:
                    pass
                else:                    
                    ano_digitado = False
                    print('Ano inválido!')
        
        # Substrair o ano atual do ano informado
        self.idade = ano_atual - self.ano_informado
        # Imprimir na tela a idade calculado    
        print("Você tem",self.idade,"anos.")
        #return (self.ano_informado, self.idade) #Tuple
    
    def __str__(self):
        return "{}/{}".format(self.nome, self.idade)

    def __repr__(self):
        return "input()={} input()=int({})".format(self.nome, self.idade)