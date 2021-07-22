# Projeto Interdisciplina SI II -  Aluna: Yasmmin Claudino
#UFRPE - 2020.1
#FlyFood

#Criação do metodo para fazer a permutação da lista de forma recursiva

def permutacoes(entrada):
    permutacaoAtual = []
    if len(entrada) <= 1:
        return [entrada]
    for i in range(len(entrada)):
        corteLista = entrada[:i] + entrada[i + 1:]
        for p in permutacoes(corteLista):
            permutacaoAtual.append([entrada[i]] + p)
    return permutacaoAtual