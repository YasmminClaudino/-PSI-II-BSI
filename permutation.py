# Projeto Interdisciplina SI II -  Aluna: Yasmmin Claudino
#UFRPE - 2020.1
#FlyFood

#Criação do metodo para fazer a permutação da lista de forma recursiva utilizando
# a palavra reservada do python yield para diminuir o gasto de memória.
#ele guarda primeira posição da lista e vai concatenando com os valores permutados
#através da recursão.
#[:indice] - primeiro elemento da permutaçao até o indice
#[indice:] - valor do indice até o ultimo elemento da permutação

def permutacoes(lista):
    if len(lista) <=1:
        yield lista
    else:
        for permutacao in permutacoes(lista[1:]):
            for indice in range(len(lista)):
                primeiroElementoLista = lista[0:1]
                yield permutacao[:indice] + primeiroElementoLista + permutacao[indice:]

#permutacoes(["A", "B", 'C', 'D'])


#