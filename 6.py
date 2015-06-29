import math

def sqformula():
	input = raw_input()
	c = 50
	h = 30
	d = input.split(',')
	print d
	print len(d)
	temp = []
	for num in range(len(d)):
		value = math.sqrt((2 * c * int(d[num]))/h)
		print value
		temp.append(str(int(round(value))))
	print ",".join(temp)

sqformula()


	