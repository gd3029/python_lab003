import matplotlib.pyplot as plt
import pylab as p

a = int (input("Podaj a = "))
x1 = p.arange(-10,0,0.5)
x2 = p.arange(0,10,0.5)

y1 = x1/(-3) + a
y2 = x2*x2/3
plt.plot(x1,y1, color="blue", label='x/(-3) + a')
plt.plot(x2,y2, color="red", label='x^x/3')
plt.xlabel("oś x")
plt.ylabel("oś y")
plt.title("Wykres funkcji")
plt.legend(loc='upper left')
plt.grid(True)


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.show()
