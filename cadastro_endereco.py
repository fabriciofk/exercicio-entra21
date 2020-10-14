#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

from cadastro_pessoa import pessoas

endereco = []

def cadastro_endereco(id_pessoa:int, rua:float, numero:int, complemento:float, bairro:float, cidade:float, estado:float):
    local = {
    'id_pessoa': id_pessoa, 
    'rua': rua,
    'numeros': numero,
    'complemento':complemento,
    'bairro':bairro,
    'cidade':cidade,
    'estado':estado}

    for chave, valor in local.items(): 
        if chave == None or valor ==' ':
            print('erro ao cadastrar ')
            break
    else:
        print('endereço concluido com sucesso ')
        endereco.append(local)


""" rua = input('qual mome da sua rua?')
numero = input('digite o numero da sua casa:') 
complemento = input('complemetm ex:loja,posto,farmacia,padaria,etx...:')
bairro = input('digite seu bairro:')
cidade = input('digite sua cidade:')
estado = input('digite seu estado:')
endereco = []

cadastro_endereco(id, rua, numero, complemento, bairro, cidade, estado)

print(endereco)
 """