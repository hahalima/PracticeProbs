def wordFrequency(n):
	input = n.split(" ")
	d = {}
	for item in input:
		if item in d:
			d[item] += 1
		elif item not in d:
			d[item] = 1
	for k, v in sorted(d.items()):
		print k, ':', v

wordFrequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")