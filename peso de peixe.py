# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
João Papo-de-Pescador, homem de bem, comprou
um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior
que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso () e calcule o excesso.
Gravar na variável excesso a quantidade de quilos
além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
'''
print('='*65)
print('PROGRAMA CALCULE O EXCESSO DE PESO DE PEIXE PESCADO E SUA MULTA')
print('='*65,'\n')

# variável peso de peixes
peso_peixe = float(input('Qual foi o total do peso dos peixes pescados: '))
#variável excesso a quantidade de quilos
total = peso_peixe
#variável multa
multa = 4.00
# Variável Regulamento máximo de kilos
regulamento = 50
# o valor da multa que João deverá pagar
if total > regulamento:
    valor = (total - regulamento) * multa
    print('*' * 87)
    print(f'Você ultrapassou os 50kg de pescado pemitidos e portanto deve pagar a multa de R${valor:.2f}')
    print('*' * 87)
# Mensagens adequadas
else:
    print('*' * 73)
    print(f'Parabéns você pescou {peso_peixe}kg e este peso estádentro dos limites do Estado')
    print('*' * 73)
