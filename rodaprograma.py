import meuprograma

ano_corrente = 2017
pode_parar = False
lista_entrevistados = []

while pode_parar == False:
    entrevistado = meuprograma.Entrevistado()  
    if entrevistado.pergunta_nome() == "parar":
        pode_parar = True
    else:
        entrevistado.pergunta_idade(ano_atual=ano_corrente)
        lista_entrevistados.append(entrevistado)

print(lista_entrevistados)