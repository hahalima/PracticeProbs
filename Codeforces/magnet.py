def magnet():
	numTimes = int(raw_input())
	count = 0
	if numTimes == 0:
		return 0;
	elif numTimes == 1:
		return 1
	userInput = raw_input()
	while ((numTimes-1) > 0):
		secondUserInput = raw_input()
		if userInput != secondUserInput:
			count += 1
			userInput = secondUserInput
		numTimes -= 1
	return count + 1 #the plus one is to include the last magnet group

print magnet()