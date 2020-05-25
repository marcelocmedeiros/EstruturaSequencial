# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

print('='*53)
print('PROGRAMA DO VALOR DO SÁLARIO PELAS HORAS DE TRABALHO')
print('='*53,'\n')

# variáveL valor da hora de trabalho e quantidade de hoas trabalhadas
print('='*45)
hora_valor = float(input('Digite o valor de uma hora de trabalho: '))
horas_trab = float(input('Qual a quantidade de hora que trabalho: '))
print('='*45, '\n')
# calculo da área do quadrado
salario = hora_valor * horas_trab
print(f'O valor do seu salário este mês foi R${salario:.2f}')

