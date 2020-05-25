# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um Programa que converta metros
'''
print('='*33)
print('PROGRAMA DE CONVERSÃO DE METROS')
print('='*33)
# variáveL
print('='*33)
metro = float(input('Digite um valor em metro: '))
print('='*50)
# operadores das conversões
print(f'Convertendo {metro:.2f}m em Kilometross temos: {metro / 10**3:.3f} km\n')
print(f'Convertendo {metro:.2f}m em Hectômetros temos: {metro / 10**2:.3f} hm\n')
print(f'Convertendo {metro:.2f}m em Decâmetros temos: {metro / 10:.2f} dam\n')
print(f'Convertendo {metro:.2f}m em Decímetros temos: {metro * 10:.2f} dm\n')
print(f'Convertendo {metro:.2f}m em Centímetros temos: {metro * 10**2:.2f} cm\n')
print(f'Convertendo {metro:.2f}m em Milímetros temos: {metro * 10**3:.2f} mm')
print('='*50)
