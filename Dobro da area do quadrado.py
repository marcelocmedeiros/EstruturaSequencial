# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.
'''

print('='*43)
print('PROGRAMA DA ÁREA DO QUADRADO E SEU DOBRO')
print('='*43,'\n')

# variável valor do lado do quadrado
print('='*43)
lado = float(input('Digite um valor do lado de um quadrado: '))
print('='*43, '\n')
# calculo da área do quadrado
area = lado * 4
print(f'A área do quadrado é: {area:.2f}\n')
# calculo do dobro da área
dobro = area * 2
print(f'O dobro da área do quadrado é:{dobro:.2f}')
