# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que
são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:

    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

    Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

print('='*35)
print('PROGRAMA DO VALOR DO CONTRACHEQUE')
print('='*35,'\n')

# variáveL valor da hora de trabalho e quantidade de hoas trabalhadas
print('='*50)
hora_valor = float(input('Digite o valor de uma hora de trabalho: '))
horas_trab = float(input('Qual foi número de hora que trabalho este mês: '))
print('='*50, '\n')
# calculo do salário no referido mês
salario_bruto = hora_valor * horas_trab
print(f'O valor do seu salário bruto este mês foi R${salario_bruto:.2f}\n')
# Calculo do Imposto de Renda - IR (11%)
ir = salario_bruto * 0.11
# calculo do quanto pagou ao INSS - (8%)
inss = salario_bruto * 0.08
# Calculo do quanto pagou ao sindicato -( 5%)
sind = salario_bruto * 0.05
# Salário Liquido
salario_liquido = salario_bruto - ir - inss - sind
print('='*50)
print(f'O valor Imposto de Renda - IR R${ir:.2f}')
print(f'O valor que você pagou ao INSS R${inss:.2f}')
print(f'O valor que você pagou ao sindicato foi R${sind:.2f}.')
print(f'O seu salário liquido este mês será R${salario_liquido:.2f}')
print('='*50)
