import numpy as np
import matplotlib.pylab as plt
#https://devarea.com/linear-regression-with-numpy/
def linear(x,y):
    m = (len(x) * np.sum(x*y) - np.sum(x) * np.sum(y)) / (len(x)*np.sum(x*x) - np.sum(x) * np.sum(x))
    b = (np.sum(y) - m *np.sum(x)) / len(x)
    return m, b

nlines = int(input("Type the number of lines: "))
data = []
min = 0
max = 3
for i in range(nlines):
    npoints = int(input("Type the number os points: "))
    points = []
    x = []
    y = []
    for j in range(npoints):
        a, b = map(float, input().split())
        if (a < min):
            min = a
        elif (a > max):
            max = a
        x.append(a)
        y.append(b)
    x = np.array(x)
    y = np.array(y)
    data.append([x,y])
print()
for i in range(len(data)):
    plt.scatter(data[i][0], data[i][1])
    m, b = linear(data[i][0],data[i][1])
    print("Line ",i,": ",m,"x + ",b, sep='')
    t = np.arange(min, max)
    plt.plot(t, t*m + b)
plt.show()
