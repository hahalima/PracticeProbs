def beautifulMatrix():
	n=1
	row = 0
	col = 0
	result = ""
	while n<=5:
		userInput = raw_input().split()
		if "1" in userInput:
			col = userInput.index("1") + 1
			row = n
			n+=1
		else:
			n+=1
	return abs(3-row)+abs(3-col)

print beautifulMatrix()