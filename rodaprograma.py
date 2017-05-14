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

print(lista_entrevistados)

for x in lista_entrevistados:
    print('O nome é {} e o ano de nascimento é {}'.format(
            x.nome,
            x.ano_informado
        )
    )