import matplotlib.pyplot as plt
from get_data import get_data

x, y = get_data()

plt.plot(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Some graph")

plt.show()