# Projeto Interdisciplina SI II -  Aluna: Yasmmin Claudino
#UFRPE - 2020.1
#FlyFood
#Criar uma matriz cheia de 0 para que possa ser preenchida
#Após criação da matriz, chega a hora de inserir os valores e salvar
#as posições de cada ponto para facilitar o calculo do danometro
#Funçao de calc do danometro que recebe os dois pontos a serem calculados
#a distancia entre eles |x1 - x2| + |y1 - y2| para que possa ser somado
#

import sys
import permutation
def lerEntrada():
    arq = open(sys.argv[1], 'r')
    linhas = arq.readlines()
    return linhas

def criarMatriz(qtdLinha, qtdColuna):
     return [[0 for x in range(qtdColuna)] for y in range(qtdLinha)]

def insereMatriz(entrada, matriz, dirPosicoes, qtdColuna,listaPosicoes):
    linha, coluna = 0, 0
    for x in entrada[1:]:
        for y in x.split():
            valor = y.split()
            if len(valor) > 0:
                elemento = valor[0]
                matriz[linha][coluna] = elemento
                setPosition(linha, coluna, elemento, dirPosicoes, listaPosicoes)
                coluna+=1
                if coluna == qtdColuna:
                    linha += 1
                    coluna = 0

def setPosition(linha, coluna, elemento, dirPosicoes, listaPosicoes):
    if elemento != "0":
        dirPosicoes[elemento] = (linha, coluna)
        if elemento != "R":
            listaPosicoes.append(elemento)
            
def getDanometro(dirPosicoes, listaPosicoes):
    listPermutation = permutation.permutacoes(listaPosicoes)
    origemRetorno= dirPosicoes["R"]
    somaAtual = 100000000000000000
    sequencia = []
    
    for casa in listPermutation:
        soma = 0
        posicaoAtual = origemRetorno
        for x in range(len(casa)):
            proximaPosicao = dirPosicoes[casa[x]]
            soma+=calculoDanometro(posicaoAtual, proximaPosicao)
            posicaoAtual = proximaPosicao
        soma+=calculoDanometro(posicaoAtual, origemRetorno) #soma o retorno

        #pode ser maior ou igual, mas optei por pegar o maior para nao trocar novamente o valor 
        if somaAtual > soma:
            somaAtual = soma
            sequencia = casa
    return(somaAtual, sequencia)

def calculoDanometro(posicaoA, posicaoB):
    x1, x2 = posicaoA[0], posicaoB[0]
    y1, y2 = posicaoA[1], posicaoB[1]
    calc = abs(x1-x2) + abs(y1-y2)
    return calc

def getResults(dirPosicoes, listaPosicoes):
    results = getDanometro(dirPosicoes, listaPosicoes)
    sequencia = ""
    for strings in results[1]:
        sequencia+= strings + " "
    return sequencia

    
    
