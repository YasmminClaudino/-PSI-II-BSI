# Projeto Interdisciplina SI II -  Aluna: Yasmmin Claudino
#UFRPE - 2020.1
#FlyFood

#Criação do metodo para fazer a permutação da lista de forma recursiva utilizando
# a palavra reservada do python yield para diminuir o gasto de memória.

def permutacoes(lista):
    if len(lista) <=1:
        yield lista
    else:
        for permutacao in permutacoes(lista[1:]):
            for indice in range(len(lista)):
                yield permutacao[:indice] + lista[0:1] + permutacao[indice:]
