# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um Programa que peça as 3 notas bimestrais e mostre a média.
'''
print('='*25)
print('PROGRAMA DA MÉDIA ESCOLAR')
print('='*25)
# variáveis notas
print('='*25)
nota_1 = float(input('Digite o 1º nota: '))
nota_2 = float(input('Digite o 2º nota: '))
nota_3 = float(input('Digite o 3º nota: '))
# Calculo da média
media = (nota_1 + nota_2 + nota_3)/3
print('='*25)
#resultado
print(f'A sua 1º nota foi {nota_1}\n'
      f'A sua 2º nota foi {nota_2}\n' 
      f'A sua 3º nota foi {nota_3}\n')
print('='*25)
print(f'A sua média foi {media:.2f}')
print('='*25)
