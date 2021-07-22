import sys

def lerEntrada():
    arq = open(sys.argv[0], 'r')
    linhas = arq.readlines()
    return linhas

def getLocais(locais):
       for x in lerEntrada():
        locais.append(x.split()[0])

def getPrimeiroElemento():
    primeiroElemento = lerEntrada()[0].split()[0]
    return primeiroElemento
