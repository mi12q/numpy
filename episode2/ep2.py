import numpy as np
import matplotlib.pyplot as plt
import glob

signals = []
new_signals = []

def mov_avg(a, n=10):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:]


for file in glob.glob("C:\\Users\\Milica\\PycharmProjects\\numpy\\episode2\\signals/*.dat"):
    data = np.loadtxt(file)
    signals.append(data)
    new_data = mov_avg(data)
    new_signals.append(new_data)

x1 = np.arange(0,100)
for i in range(len(signals)):
    y1 = signals[i]
    y2 = new_signals[i]
    y2 = y2/10
    x2 = np.linspace(0,100, len(y2))
    name1 = str(i+1)+ ".png"
    name2 = "filtered"+str(i+1)+".png"

    plt.figure()
    plt.plot(x1,y1)
    plt.grid()
    plt.title("Сырой сигнал")
    plt.savefig(name1)
    plt.close()

    plt.figure()
    plt.plot(x2,y2)
    plt.grid()
    plt.title("После фиьтра")
    plt.savefig(name2)
    plt.close()
