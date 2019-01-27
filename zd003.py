import matplotlib.pyplot as plt
import numpy as np
import random

n = int(input("Podaj liczbę kroków: "))
x = y = 0
lx = [0]
ly = [0]

for i in range(0, n):
    rad = float(random.randint(0, 360)) * np.pi / 180
    x = x + np.cos(rad)
    y = y + np.sin(rad)
    lx.append(x)
    ly.append(y)

print(lx, ly)

s = np.fabs(np.sqrt(x**2 + y**2))
print("Wektor przesunięcia:", s)
plt.plot([0, x], [0, y], 'k-', lw=2, color="red")

plt.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")
plt.xlabel("lx")
plt.ylabel("ly")
plt.title("Ruchy Browna")
plt.grid(True)
plt.show()
