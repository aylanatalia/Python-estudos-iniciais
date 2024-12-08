# ESTRUTURAS CONDICIONAIS

idade = 18

#criando a condicional
if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

media = float(input('Informe a média do aluno:'))

#Usando o elif que tem a mesma função de else if para criar mais uma condicional
if media >= 7:
    print('Você foi aprovado.')
elif media >= 5:
    print('Recuperação.')
else:
    print('Você foi reprovado.') 


media_nota = 10
presenca = 100

#o uso do and torna necessário que as duas condições devem ser verdadeiras
if media_nota >= 7 and presenca >= 70:
    print('Aprovado')
else:
    print('Reprovado')