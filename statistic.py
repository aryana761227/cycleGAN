import matplotlib.pyplot as plt
l = open("stoch.txt", "r")
x = []
for i in l:
    x = i.split()
X = []
Y = []
for i in range(6, len(x), 7):
    X.append(int((i-6)/7))
    Y.append(float(x[i]))

plt.plot(X, Y)
plt.show()
