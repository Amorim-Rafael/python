import meuprograma

pode_parar = False
lista_entrevistados = []

while pode_parar == False:
    entrevistado = meuprograma.Entrevistado()  
    if entrevistado.pergunta_nome() == "parar":
        pode_parar = True
    else:
        entrevistado.pergunta_idade()
        lista_entrevistados.append(entrevistado)

print(lista_entrevistados)

for x in lista_entrevistados:
    print("O nome é {} e o ano de nascimento é {}".format(
            x.nome,
            x.ano_informado
        )
    )