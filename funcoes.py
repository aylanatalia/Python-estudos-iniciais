#Criando uma função 
# função para imprimir uma saudação
def saudacao():
    print('Seja bem vindo')
    print('Olá, é um prazer te ter nesse curso')

#chamando uma função
saudacao() 

#criando uma função com o parametro
def saudacao1(nome, curso):
    print(f'Seja Bem vindo {nome}') 
    print(f'É um prazer ter você nesse curso de {curso}')

saudacao1('Ayla Natalia', 'Python')

#criando uma função com parametro default, que tenha um valor padrão caso a gente não preencha um valor
def saudacao2(nome, curso='Python'):
    print(f'Seja Bem vindo {nome}') 
    print(f'É um prazer ter você nesse curso de {curso}')

saudacao2('Ayla Natalia')

#funções com retorno
def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 7)
print('O resultado da soma é:', resultado)

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2

resultado = calculadora(10,20)
print('Resultado é:', resultado)