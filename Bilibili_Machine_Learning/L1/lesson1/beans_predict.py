"""
This is a simple McCulloch - Pitts model
"""

import dataset
from matplotlib import pyplot as plt

xs,ys = dataset.get_beans(100)

print(xs)
print(ys)

# configure figure settings
plt.title("Size-Toxicity function", fontsize=12)
plt.xlabel("Bean size")
plt.ylabel("Toxicity")

plt.scatter(xs,ys)

# set function y = 0.5x
w = 0.5
y_pre = w * xs
plt.plot(xs, y_pre)



plt.show()