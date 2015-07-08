def epicGame():
	userInput = "1 1 100"
	a,b,n = map(int, userInput.split())
	while n > 0:
		gdcA = gcdIter(a, n)
		if gdcA <= n:
			n -= gdcA
		elif n == 0:
			return 0
		gdcB = gcdIter(b, n)
		if gdcB <= n:
			n -= gdcB
		elif n == 0:
			return 0


def euclid(a,b):
	if a%b == 0:
		return a/b
	if b > a:
		return 1
	else:
		euclid(b, a%b)

print euclid(210,45)