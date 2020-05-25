# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
 e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
 Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
print('='*80)
print('PROGRAMA CALCULE QUANTIDADE DE LATAS DE TINTA A SEREM COMPRADAS E O PREÇO TOTAL')
print('='*80,'\n')

# variável tamanho em metros quadrados da área a ser pintada
area = int(input('Qual tamanho em metros quadrados da área a ser pintada: '))
# variável cobertura
litros = area / 3
# Calculo da quantidades de latas de tinta a serem compradas
if area % 54 == 0:
    latas = area / 54
else:
    latas = int(area/54)+1
# o preço
preco = latas * 80
print(f'A quantidade de latas é {latas}')
print(f'O valor a pagar é R${preco:.2f}')

