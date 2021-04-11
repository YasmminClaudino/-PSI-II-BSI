import matplotlib.pyplot as plt
import main

x, y = [], []
dirPosicoes = main.dirPosicoes
results = main.results

def plotarGrafico():
       for i in results.split():
              setPosicaoGrafico(i, dirPosicoes)

def setPosicaoGrafico(i, dirPosicoes):
       x.append(dirPosicoes[i][0])
       y.append(dirPosicoes[i][1])

plotarGrafico()

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(title='Menor Rota')
ax.grid()

fig.savefig("test.png")
plt.show()