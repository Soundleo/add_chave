# dicionário
import os


pessoa = {
    'Nome'  : 'Leandro Peres',
    'Idade' : 38,
    'Profissão' : 'Bancário'
}

for i in pessoa:
    print(f'{i}: {pessoa.get(i)}')

nova_chave = input('Digite o nome do campo que deseja criar: ').capitalize()
novo_valor = input(f'Informe o valor do campo {nova_chave}: ' ).capitalize()
pessoa [nova_chave] = novo_valor

os.system('cls')

# imprime novo dicionário

for i in pessoa:
    print(f'{i}: {pessoa.get(i)}')