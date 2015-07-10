def stickGame():
	n, k = map(int, raw_input().split())
	winner = ""
	matrix = [[0 for num in range(n)] for num in range(k)]
	while True:
		if n == 0 or k == 0:
			winner = "Malvika"
			break;
		else:
			n-=1
			k-=1
			matrix = [[0 for num in range(n)] for num in range(k)]
		if n == 0 or k == 0:
			winner = "Akshat"
			break;
		else:
			n-=1
			k-=1
			matrix = [[0 for num in range(n)] for num in range(k)]
	return winner


print stickGame()