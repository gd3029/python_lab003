import matplotlib.pyplot as plt
import pylab as p

a = int (input("Podaj a = "))
b = int (input("Podaj b = "))
x = p.arange(-10,10,0.5)

y = a*x+b
plt.plot(x,y, label='Funkcja \nliniowa')
plt.title("Wykres f(x) = a*x +b")
plt.legend(loc='upper left')
plt.grid(True)
if a < 0:
    plt.text(1, b+0.25,"Funkcja malejąca")
elif a == 0:
    plt.text(1, b,"Funkcja stała")
else:
    plt.text(1, b+0.25,"Funkcja rosnąca")

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.show()
