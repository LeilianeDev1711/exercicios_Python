''' Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). '''

import math

tamanho = float(input("Insira o tamanho do arquivo em MB: "))
velocidade = float(input("Insira a velocidade de internet (MBps): "))
tempo = math.ceil(tamanho / velocidade)
print("Tempo aproximadamente de download: {} minutos".format(tempo))
