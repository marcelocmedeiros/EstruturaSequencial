# Marcelo Campos de Medeiros
# ADS UNIFIP 2020.1
# Patos-PB 17/03/2020

'''
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e
informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
print('=' * 55)
print('PROGRAMA CALCULE O TEMPO APROXIMADO DE UM DOWNLOAD')
print('=' * 55, '\n')

# variável tamanho de um arquivo para download (em MB)
arquivo = float(input('Qual o tamanho de um arquivo para download (em MB): '))
# variável velocidade de um link de Internet (em Mbps)
velocidade = float(input('Qual a velocidade de um link de Internet (em Mbps): '))
tempo = ((arquivo * 8) / velocidade) / 60
print('*' * 110)
print(f'O tempo aproximado de download do arquivo {arquivo}MB '
      f'usando este link de velocidade {velocidade}Mbps é de {tempo:.2f} min')
print('*' * 110)