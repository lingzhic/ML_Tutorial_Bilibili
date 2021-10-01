import numpy as np


def get_beans(counts):
	# x for bean size, y for bean toxicity
	xs = np.random.rand(counts)
	xs = np.sort(xs)
	ys = [1.2*x+np.random.rand()/10 for x in xs]
	return xs,ys

