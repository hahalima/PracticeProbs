def ultraFastMathMan():
	index = 0
	result = ""
	lineOne = raw_input()
	lineTwo = raw_input()
	for n in lineOne:
		if n == lineTwo[index]:
			result = result + "0"
		else:
			result = result + "1"
		index += 1
	return result

print ultraFastMathMan()