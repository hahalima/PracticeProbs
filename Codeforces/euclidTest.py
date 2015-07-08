def euclid(a,b):
	if a%b == 0:
		return a/b
	if b > a:
		return 1
	else:
		euclid(b, a%b)

print euclid(210,45)