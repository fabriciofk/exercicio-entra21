#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve exibir todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
        #a função deve exibir uma pessoa cadastrada na função do ex1 filtrando por id

import cadastro_pessoa
from cadastro_pessoa import cadastros

def mostrar_pessoas():
    return cadastro_pessoa.pessoas 

def pessoa_por_id(id_pessoa):
    lista = mostrar_pessoas()
    for pessoas in lista:
        if id_pessoa == pessoas['id']:
            return pessoas
    print('O id não cadastrado:')

