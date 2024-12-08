idade = '26'

print(idade, type(idade))

#conveter o tipo da variável idade de str para int
idade_inteira = int(idade)

print(idade_inteira, type(idade_inteira))

"""
PARA CONVERTER VALORES USE AS FUNÇÕES
int()
str()
float()
bool()
"""

# assim conseguiremos converter os valores digitado pelo usuário para que não fique no tipo str
altura = float(input('Digite sua altura:'))
print(altura, type(altura))
