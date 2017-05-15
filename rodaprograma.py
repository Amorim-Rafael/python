import meuprograma
import statistics

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

# Lista por Compreensão
# lista = [<expresao para valor> <loop> <expressao para o loop>]
# lista_idades = [item.idade for item in lista_entrevistados]
menor_idade = min([item.idade for item in lista_entrevistados])
maior_idade = max([item.idade for item in lista_entrevistados])
media_adulto = statistics.median_high([item.idade for item in lista_entrevistados if item.idade >= 18])

# Mostrar a quantidade de nascimentos por decada
# O que temos: [1971, 1982, 2003, 1995, 1976]

# 1º passo: converter anos em decadas
# 2º passo: criar uma lista nova com decadas sem repetir
# 3º passo: contar as decadas da lista original na lista nova
# Para cada decada dentro da lista nova (set) contar qtas vezes ela aparece na lista original
# Dicionário por Compreensão
# dicionario = { <expressao para a chave>:<expressao para o valor> <loop> <expressao para o loop> }
# O que queremos: [1970:2, 1980:5, 1990:1, 2000:2]

# 1985 / 10 = 198,5 int > 198 * 10 = 1980
lista_decadas = [int(item.ano_informado/10)*10 for item in lista_entrevistados]
# set(): lista que valores não se repetem e não podem ser ordenadas
set_decadas = set(lista_decadas)
qtd_nascimentos = { decada:lista_decadas.count(decada) for decada in set_decadas }

# print('lista_decadas:',lista_decadas)
# print('set_decadas:',set_decadas)
# print('qtd_nascimentos:',qtd_nascimentos)
# print('Menor idade é:',menor_idade)
# print('Maior idade é:',maior_idade)
# print('Media idade adulto:',media_adulto)

print('\nResultados:')
print('---------------------------------------')
print('Quantidade de entrevistas: {}'.format(len(lista_entrevistados)))
print('Menor idade: {}'.format(menor_idade))
print('Maior idade: {}'.format(maior_idade))
print('Média de idade dos adultos: {}'.format(media_adulto))
print('\nNascimentos por Década')
print('---------------------------------------')
for decada, quantidade in qtd_nascimentos.items():
    print('{}: {} nascimento(s)'.format(decada, quantidade))
print('\n')    