# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
'''
print('='*35)
print('PROGRAMA PARA CALCULAR PESO IDEAL')
print('='*35,'\n')

# variável altura de uma pessoa
print('='*27)
altura = float(input('Qual é sua altura: '))
print('='*27, '\n')
# calculo do peso ideal fórmula: (72.7*altura) - 58
peso = (72.7 * altura) - 58
print('*'*50)
print(f'Seu peso idela para sua altura de {altura}m é {peso:.2f}kg')
print('*'*50)
