# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Tendo como dado de entrada a altura (h) de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
'''
print('='*43)
print('PROGRAMA PESO IDEAL PARA MULHERES E HOMENS')
print('='*43,'\n')

# variável sexo masculino ou feminino
print('='*65)
sexo = str(input('A que tipo de genero você pertence F(feminino) e M(masculino): ')).strip().upper()
# variável altura da pessoa
print('='*27)
altura = float(input('Qual é sua altura: '))
print('='*27, '\n')
# calculo do peso ideal para homens fórmula: (72.7*altura) - 58
if sexo == 'M':
    peso = (72.7 * altura) - 58
    print('*'*50)
    print(f'Seu peso idela para sua altura de {altura} m é {peso:.2f}kg')
    print('*'*50)
# calculo do peso ideal para mulheres fórmula: (62.1*h) - 44.7
else:
    peso = (62.1 * altura) - 44.7
    print('*' * 50)
    print(f'Seu peso idela para sua altura de {altura} m é {peso:.2f}kg')
    print('*' * 50)

