# Estruturas de listas
# criando uma lista de notas
notas = [7.9, 9.7, 8.2]

#criando uma lista vazia 
lista = []
lista = list()
# a lista pode conter tipos de elementos diferentes
lista = [27, 'Ayla', 3.1415, False]
# é possível criar uma lista que contenha outra lista em seus elementos
lista_de_lista = [10, [1, 2, 3]]

# Indexação e slice(fatiamento)
lista = [10, 'Ayla Natalia', 1.88, True]
# acessando o elemento através do index
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
#caso coloque indice negativo ele contará do ultimo para o primeiro
print(lista[-1])

#slice
lista = [10, 50, 30, 40, 25, 60, 5]
# ele irá imprimir os elementos do indice 0 a menor que 3
print(lista[0:3])

#usando for para percorrer os elementos da lista
for elemento in lista:
    print(elemento)

# percorrer os elementos da lista usando o tamanho
print('Comprimento da lista: ', len(lista))

for i in range(len(lista)):
    print(lista[i])

# Métpdp de listas
lista = [1, 3, 12, 8, 2]
print('Lista antes do append: ', lista)

#append para adicionar elementos ao final da lista
lista.append(3)
print('Lista depois do append: ', lista)

#insert adiciona elemento a lista escolhendo a posição que ele vai ser inserido
lista.insert(2, 10)
print('Lista depois do insert: ', lista)

#extend junta duas listas colocando a segunda lista e colocando no final da lista
lista2 = [1, 2, 3]
lista.extend(lista2)
print('Lista depois do extend: ', lista)

# pop remove o elemento especificado ou o ultimo elemento
lista.pop()
print('Lista depois do pop: ', lista)
lista.pop(0)
print('Lista depois do pop no indece 0: ', lista)

#remove remove o elemento que eu disser especificando o valor
lista.remove(3)
print('Lista depois do remove:', lista)

#count para contar a quantidade que o elemento aparece
print('Quantidade de 2 na lista: ', lista.count(2))

#index para descobrir o indice do elemento
print('Indice do elemento 12:', lista.index(12))

#sort ordena a lista em ordem crescente
lista.sort()
print('Lista depois do sort:', lista)
#para ficar decrescente lista.sort(reverse = True)

#Funções de lista
#len conta a quantidade de elementos da lista
print('Comprimento da lista: ', len(lista))

#sum soma todos os elementos da lista
print('Soma dos elementos da lista:', sum(lista))

#max retorna o maior valor da lista
print('Maior valor da lista:', max(lista))

#min retorna o menor valor da lista
print('Menor valor da lista:', min(lista))