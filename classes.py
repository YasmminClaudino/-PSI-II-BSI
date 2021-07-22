import math
import random

random.seed(15151561)

class AlgoritmoGenetico:
    def __init__(self, tamnhoPopulacao, semente, geracao, primeiroElemento):
        self.tamanhoPopulacao = tamnhoPopulacao
        self.semente = semente
        self.geracao = geracao
        self.melhorRota = primeiroElemento

    def populacaoInicial(self, locais, primeiroIndiviuo):
        populacao = Populacao(primeiroIndiviuo)
        listaIndividuosAleatória = random.sample(locais, len(locais))
        populacao.inidiviuos = [Rota(listaIndividuosAleatória) for i in range(self.tamanhoPopulacao)]

    def mutacao(individuo):
        chances = random.random()
        for i in range(1, len(individuo)-1):
            if (chances < 0.2):

                while random.randrange(1, len(individuo)) == 0 or random.randrange(1, len(individuo)) == len(individuo)-1:
                    j = random.randrange(1, len(individuo)-1)
                temp = individuo[j]
                individuo[j] = individuo[i]
                individuo[i] = temp
        return individuo

    def torneio(populacao):
        chances = random.choices(populacao.inidiviuos)
        melhorIndividuo = None
        maisApto = 400000000000000000000.0000000

        for i in chances:
            distancia = Rota.distanciaDosPontos(i)
            if distancia < maisApto:
                maisApto = distancia
                melhorIndividuo = i
        return melhorIndividuo

    def melhorDistancia(self):
        populacao = self.novaGeracao(populacao, 3, 0.6, 0.02)

        populacao = [Rota(populacao) for i in range(self.tamanhoPopulacao)]
        melhorRota = populacao.individuos[0]
        menorDistancia = Rota.distanciaDosPontos(melhorRota)

        return menorDistancia

    def novaGeracao(populacao, param, param1, param2):
        # TODO
        pass


class Populacao:
    def __init__(self, melhorIndividuo):
        self.inidiviuos = []
        self.melhorIndividuo = melhorIndividuo
    def __repr__(self):
        return self.inidiviuos

class Rota:
    def __init__(self,rota, aptidao=None):
        self.rota = rota
        self.aptdao = aptidao

    def distanciaDosPontos(self, sequencia):
            distancia = 0
            for i in range(len(sequencia) - 1):
                pontoAtual = sequencia[i]
                proximoPonto = sequencia[i + 1]
                distancia += (pontoAtual.calculoDistancia(proximoPonto))
            return distancia

class Pontos:
    def __init__(self, pontoX, pontoY):
        self.pontoX = pontoX
        self.pontoY = pontoY

    def calculoDistanciaEuclidiana(self, Ponto1, Ponto2):
        distanciaX = (Ponto1.x - Ponto2.x)
        distanciaY = (Ponto1.y - Ponto2.y)
        raizX = math.sqrt(distanciaX)
        raizY = math.sqrt(distanciaY)
        distancia = int(raizX + raizY)
        return distancia
