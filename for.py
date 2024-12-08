# estrutura de repetição controlada com for
#range é uma faixa de valores, no caso do exemplo, de 0 a 9
for variavel in range(10):
    print(variavel)

#range de 1 a 9 informado o valor de inicio e de fim
for variavel in range(1, 10):
    print(variavel)

#range com valor de início e de fim e o valor de quantos em quantos sera contado, por exemplo, de 3 em e
for variavel in range(1, 12, 3):
    print(variavel)

"""
construindo esse código abaixo usando for
nota1 = float(input('Informe sua nota 1:'))
nota2 = float(input('Informe sua nota 2:'))
nota3 = float(input('Informe sua nota 3:'))
"""

soma = 0
#f str- quando eu coloco f antes de uma string você pode injetar um a variável dentro dela
for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}:'))
    soma = soma + nota
print(soma / 3)