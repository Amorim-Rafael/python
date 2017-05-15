import meuprograma

pode_parar = False
lista_entrevistados = []

while pode_parar == False:
    entrevistado = meuprograma.Entrevistado()  
    # lower() deixa as letras minusculas
    if entrevistado.pergunta_nome().lower() == 'parar':
        pode_parar = True
    else:
        try:
            entrevistado.pergunta_idade()
            # x = 1000/0            
        except ZeroDivisionError:
            print('Ocorreu um erro, mais o entrevistado foi inserido na lista!')        
            lista_entrevistados.append(entrevistado)
        except Exception as erro:
            print('Ocorreu um erro e lista não foi salva!')
            print('O tipo de erro foi {}'.format(type(erro)))
            print('A mensagem de erro é {}'.format(erro))
        else:
            lista_entrevistados.append(entrevistado)


# Mostrar a menor idade calculada
# Mostrar a maior idade calculada
# Mostrar a media de idade calculada
# Mostrar a quantidade de nascimentos por decada


# lista_idades = []
# Preenchimento comum de uma lista 
# for item in lista_entrevistados:
#     lista_idades.append(item.idade)

# menor_idade = min(lista_idades)
# maior_idade = max(lista_idades)

# Lista por Compreensão
# lista = [expresao loop]
# lista_idades = [item.idade for item in lista_entrevistados]
menor_idade = min([item.idade for item in lista_entrevistados])
maior_idade = max([item.idade for item in lista_entrevistados])

print('Menor idade é:',menor_idade)
print('Maior idade é:',maior_idade)