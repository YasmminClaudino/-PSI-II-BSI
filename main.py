# Projeto Interdisciplina SI II -  Aluna: Yasmmin Claudino
#UFRPE - 2020.1
#FlyFood
#dic utilizado para guardar as posições de cada "casa".
#Lista para guardar as posições que será feita as permutações
#Arquivo de entrada é dado através de um arquivo que pode ser colocado os valores

import functions
import plotarGrafico

matriz, listaPosicoes = [], []
dirPosicoes = {}

entrada = functions.lerEntrada()
qtdLinha = int(entrada[0].split()[0])
qtdColuna = int(entrada[0].split()[1])
matriz = functions.criarMatriz(qtdLinha,qtdColuna)
functions.insereMatriz(entrada, matriz, dirPosicoes, qtdColuna, listaPosicoes)
results = functions.getResults(dirPosicoes, listaPosicoes)

print(results)
