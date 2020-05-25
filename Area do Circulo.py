# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''

print('='*33)
print('PROGRAMA DA ÁREA DO CÍRCULO')
print('='*33,'\n')

# variáveL
print('='*40)
raio = float(input('Digite um valor do raio de um círculo: '))
print('='*40)
# calculo da área do círculo
area = raio **2 * 3.14
print(f'A área do círculo é: {area:.2f}\n')
print(f'Ou podemos dizer que a área do círculo é:', raio ** 2,'π')
