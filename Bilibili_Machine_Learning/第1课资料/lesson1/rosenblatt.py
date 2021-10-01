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

'''
# a single adjustment of w
x = xs[0]
y = ys[0]
y_pre = w * x
err = y - y_pre
alpha = 0.05    # adjusting factor
w = w + alpha * err * x
'''

'''
# a single loop adjustment of w
alpha = 0.05  # adjusting factor
for i in range(100):
    x = xs[i]
    y = ys[i]
    y_pre = w * x
    err = y - y_pre
    w = w + alpha * err * x
'''


alpha = 0.05  # adjusting factor
for m in range(100):
    for i in range(100):
        x = xs[i]
        y = ys[i]
        y_pre = w * x
        err = y - y_pre
        w = w + alpha * err * x


y_pre = w * xs
plt.plot(xs, y_pre)



plt.show()