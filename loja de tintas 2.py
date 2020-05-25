# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros,que custam R$ 80,00
ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
print('='*35)
print('PROGRAMA PARA UMA LOJA DE TINTAS')
print('='*35,'\n')

# variável tamanho em metros quadrados da área a ser pintada
area = float(input('Qual tamanho em metros quadrados da área a ser pintada: '))
# variáveis
cobertura = 6
lata = 18
galao = 3.6
preco_lata = 80.00
preco_galao = 25.00
area_lata = lata * cobertura
area_galao = galao * cobertura
#10% de folga no cálculo da área
area_folga = area + (area * 0.10)
num_lata = 0
num_galao = 0
total_pagar = 0
#Cálculo de utilização de latas
if area_folga <= area_lata:
    num_lata = 1
    total_pagar = preco_lata
    print(f"A) Será necessária {num_lata} lata e o valor a pagar é R$ {total_pagar:.2f}")
else:
    num_lata = int(area_folga / area_lata) + 1
    total_pagar = num_lata * preco_lata
    print(f"A) Serão necessárias {num_lata} latas e o valor a pagar é R$ {total_pagar:.2f}")
#Cálculo de utilização de Galões
if area_folga <= area_galao:
    num_galao = 1
    total_pagar = preco_galao
    print(f"A) Será necessária {num_galao} lata e o valor a pagar é R$ {total_pagar:.2f}")
else:
    num_galao = int(area_folga / area_galao) + 1
    total_pagar = num_galao * preco_galao
    print(f"B) Serão necessárias {num_galao} galão e o valor a pagar é R$ {total_pagar:.2f}")
# Cálculo de misto Latas e galões
 # Cada 3 galões compensa financeiramente em relação 01 lata
if area_folga <= (area_galao * 3):
    num_lata = 0
    num_galao = int(area_folga / area_galao) + 1
    total_pagar = num_galao * preco_galao
    print(f"C) Serão necessários {num_lata} latas e {num_galao} galões e o valor a pagar é R$ {total_pagar:.2f}" )
elif area_folga > (area_galao * 3) and area_folga < area_galao:
    num_galao = 0
    num_lata = 1
    total_pagar = preco_lata
    print(f"C) Serão necessários {num_lata} latas e {num_galao} galões e o valor a pagar é R$ {total_pagar}" )
else:
    # Caso a área seja maior que o rendimento de 1 lata
    num_lata = int(area_folga / area_lata)
    # resto da divisão por latas será a área a ser dividida em galões + 1
    num_galao = int((area_folga % area_lata) / area_galao) + 1
    total_pagar = (num_lata * preco_lata) + (num_galao * preco_galao)
    print(f"C) Serão necessários {num_lata} latas e {num_galao} galões e o valor a pagar é R$ {total_pagar:.2f}" )