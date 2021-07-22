import matplotlib.pyplot as plt


x = [2,2,7,9,50,300,700]
y = [4,6,7,8,9,10,11]


fig, ax = plt.subplots()
ax.plot(y, x, c='b')
ax.set(title="Tempo por segundo AG - Roleta")
fig.savefig("Teste.png")
fig, ax = plt.subplots()
plt.show()