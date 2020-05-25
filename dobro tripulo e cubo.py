# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um Programa que peça 2 números inteiros e um número real.
    Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.
'''
print('='*40)
print('PROGRAMA PARA CALCULAR UMA EXPRESSÃO')
print('='*40,'\n')

# variável dois números inteiros
print('='*33)
num_1 = int(input('Digite o 1° número inteiro: '))
num_2 = int(input('Digite o 2° númerointeiro: '))
num_3 = float(input('Digite o 3° número real: '))
print('='*33, '\n')
# calculo do produto do dobro do primeiro com metade do segundo
calc_1 = (num_1 * 2) + (num_2 / 2)
print('*'*58)
print(f'O produto do dobro do primeiro com metade do segundo é {calc_1:.0f}')
print('*'*58)
# a soma do triplo do primeiro com o terceiro
calc_2 = (num_1 * 3) + num_3
print(f'A soma do triplo do primeiro com o terceiro é {calc_2:.2f}')
print('*'*58)
# o terceiro elevado ao cubo
calc_3 = num_3**3
print(f'O terceiro elevado ao cubo é {calc_3:.2f}')
print('*'*58)