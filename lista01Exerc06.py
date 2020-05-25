# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020
# Listas de exercícios Lista 01
'''
6 - Escreva um programa que leia uma temperatura em graus Fahrenheit,
transforme-a em graus Celsius e exiba o resultado.
'''

print('='*40)
print('PROGRAMA DE CONVERSÃO DE TEMPERATURAS')
print('='*40,'\n')

# variável valor da temperatura
print('='*43)
temp_faren = float(input('Digite a temperatura em Farenheit: '))
print('='*43, '\n')
# calculo da conversão para Celsius
print('*'*58)
temp_cels = (5 * (temp_faren-32) / 9)
print(f'O valor da temperatura em de {temp_faren}°F em Celsius é {temp_cels:.2f}°C')
print('*'*58)
# calculo da conversão para Kelvin
temp_kelv = temp_cels + 273.15
print(f'O valor da temperatura em de {temp_faren}°F em Kelvin é {temp_kelv:.2f}°K')
print('*'*58)
