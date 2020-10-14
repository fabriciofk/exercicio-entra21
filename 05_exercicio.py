#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
                #com seus respectivos endereços utilizando as funções do ex3 e ex4
from cadastro_endereco import cadastro_endereco
from cadastro_pessoa import cadastros
from funcoes import mostrar_pessoas
from funcao_endeco import monstra_endereco


def lin ():
    print('-'*80)

print('''
    ############################################################################
    #################SEJA BEM VINDO A CENTRAL DE CADASTRAMENTO:#################
    ############################################################################
'''.format())


while True: 
    nome = input('digite seu nome:')
    lin()
    sobrenome = input('digite seu sobrenome:')
    lin()
    idade = int(input('digite sua idade'))
    lin()

    cadastro = cadastros(nome, sobrenome, idade)
    lin()
    rua = input('digite sua rua:')
    lin()
    numero = input('digite o numero da casa:')
    lin()
    complemento = input('digite o complemento:')
    lin()
    bairro = input('digite o bairro:')
    lin()
    cidade = input('digite a cidade:')
    lin()   
    estado = input('digite seu estado:')
    lin()
    cadastro_endereco(cadastro, rua, numero, complemento, bairro, cidade, estado)
    loop = input('continuar cadastrando? (S/N): ')
    if loop.upper() == 'N':
        break

lista_pessoa = mostrar_pessoas()
lista_endereco = monstra_endereco()

print('exibindo pessoas:')

lin()
for pessoas in lista_pessoa:
    print(f'id: {pessoas["id"]}')
    print(f'nome: {pessoas["nome"]}')
    print(f'sobrenome: {pessoas["sobrenome"]}')
    print(f'idade: {pessoas["idade"]}')
print('EXIBINDO ENDEREÇOS')
lin()
for endereco in lista_endereco:
    print(f'id_pessoa: {endereco["id_pessoa"]}')
    print(f'rua: {endereco["rua"]}')
    print(f'numeros: {endereco["numeros"]}')
    print(f'complemento: {endereco["complemento"]}')
    print(f'bairro: {endereco["bairro"]}')
    print(f'cidade: {endereco["cidade"]}')
    print(f'estado: {endereco["estado"]}')
lin()

