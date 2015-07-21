def youngPhysicist():
	numTimes = int(raw_input())
	result = [0,0,0]
	while (numTimes > 0):
		userInput = [int(x) for x in raw_input().split()]
		for n in range(0,3):
			result[n] += userInput[n]
		numTimes -= 1
	if (result == [0,0,0]):
		return "YES"
	else:
		return "NO"

print youngPhysicist()