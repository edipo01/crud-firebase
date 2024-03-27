import requests
import  json

# Banco de dados
linkBD = "https://projetos-teste-br-default-rtdb.firebaseio.com"

# Inserindo dados
# dados = {'Quantidade': '11', 'preço': 100, 'produto':'Vestido'}
# requisicao = requests.post(f'{linkBD}/Produtos/.json', data=json.dumps(dados))

# print(requisicao)
# print(requisicao.text)

# Alterando os dados
# dados = {'quantidade': 20, 'preco': 140, 'produto': 'Calça Jeans'}
# requisicao = requests.patch(f'{linkBD}/Produtos/-NtsKA-jGd91Dgz6iuk9/.json', data=json.dumps(dados))
# print(requisicao.status_code)
# print(requisicao.text)
# print(requisicao)

# Pegar uma venda especifica
requisicao = requests.get(f'{linkBD}/Vendas/.json' )
print(requisicao)
# print(requisicao.text)

# Transformando em dicionario 
dict_requisicao = requisicao.json()
id_db = None
# Iterando
for id_venda in dict_requisicao:
    cliente = dict_requisicao[id_venda]['cliente']
    if cliente == "alon":
        print(f'----> {id_venda}')
        id_db = id_venda
        print(f'Encontrado: {id_db}')

# Remover um produto da base de dados
requisicao = requests.delete(f'{linkBD}/Vendas/{id_db}/.json')
print(requisicao)
print(requisicao.text)