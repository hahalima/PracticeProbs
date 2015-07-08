def bitPlusPlus():
	numberOfTimes = int(raw_input())
	result = 0
	while numberOfTimes>0:
		statement = raw_input().lower()
		if (statement == "++x" or statement == "x++"):
			result+= 1
		elif (statement == "--x" or statement == "x--"):
			result-= 1
		numberOfTimes-= 1
	return result
print bitPlusPlus()