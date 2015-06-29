def xy2d(x,y):
	matrix = [[0 for i in xrange(y)] for i in xrange(x)]
	for i in range(x):
		for j in range(y):
			matrix[i][j] = i * j
	return matrix

def xy2d2(x, y):
	return [[i*j for i in xrange(y)] for j in xrange(x)]

print xy2d(3,5)
print xy2d2(3,5)