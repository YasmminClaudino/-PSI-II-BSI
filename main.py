from classes import *
from lerEntrada import *

tamnhoPopulacao = 60
semente = 1541515614
geracao = 1000
elitismo = 3
mutacao = 0.02
crossover = 0.6
l = []
locais = getLocais(l)
primeiroElemento = getPrimeiroElemento()
menorDistancia = 0


ca = AlgoritmoGenetico(tamnhoPopulacao, semente, geracao, primeiroElemento)
ca.populacaoInicial(l, primeiroElemento)

for i in range(1, geracao + 1):
    menorDistancia = ca.melhorDistancia()

print(menorDistancia)