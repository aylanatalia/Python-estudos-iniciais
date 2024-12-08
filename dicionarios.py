#Criando um dicionario
dicionario = {}
dicionario = dict()
dicionario = {'nome': 'Ayla Natalia', 'idade': 27, 'altura': 1.88}
print(dicionario)

#acessando um dado do dicionario
print(dicionario['idade'])

#adicionando elementos no dicionario
dicionario['programador'] = True
print(dicionario)

#adicionando elemento sobrescrevendo o elemento já existente
dicionario['altura'] = 2
print(dicionario)

#percorrendo os elementos do dicionario e imprimindo as chaves
for variavel in dicionario:
    print(variavel)

#imprimindo os valores da chave
for chave in dicionario:
    print(chave, dicionario)

#verificando a existencia de uma chave
print('peso' in dicionario)
print('altura' in dicionario)