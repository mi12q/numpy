import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter

all_data = []
data = np.loadtxt("C:\\Users\\Milica\\PycharmProjects\\numpy\\episode3\\start.dat")
all_data.append(data)
x = np.linspace(0,50,len(data))
plt.plot(x,data)
plt.xlim(0,50)
plt.ylim(0,10)
plt.grid()
plt.savefig('initial.png')
plt.close()

n = len(data)
A = np.zeros((n,n),float)
A.flat[0::n+1] = 1
A.flat[n::n+1] = -1

print(A)

for i in range(0,255):
    data = data - 0.5 * np.matmul(A,data)
    all_data.append(data)

fig, ax = plt.subplots()


def animate(i):
    ax.clear()
    y = all_data[i]
    x = np.linspace(0, 50, len(y))
    ax.plot(x, y)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 10)
    ax.grid()
    ax.plot(x,y)


anim = FuncAnimation(fig, animate, frames=255, interval=500, repeat=False)
anim.save("animation.gif", dpi=300,
         writer=PillowWriter(fps=5))

plt.show()
