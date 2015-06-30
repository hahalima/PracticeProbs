def calcUpperLower(n):
	upper = 0
	lower = 0
	for char in n:
		if char.isupper():
			upper+=1
		elif char.islower():
			lower+=1
	print "UPPER CASE: " + str(upper)
	print "LOWER CASE: " + str(lower)

calcUpperLower("Hello world!")