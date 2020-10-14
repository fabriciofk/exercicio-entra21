#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve exibir todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
        #a função deve exibir um endereço cadastrado na função do ex2 filtrando por 
           # id da pessoa
import cadastro_endereco

def monstra_endereco():
    return cadastro_endereco.endereco

def id_pessoa_endereco(id_pessoa):
    modo = monstra_endereco()
    for endereco in modo:
        if id_pessoa == endereco(id_pessoa):
            return endereco
    print('id nao encontrado:')

