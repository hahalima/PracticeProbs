def stringTask():
	userInput = raw_input().lower()
	result = ""
	for char in userInput:
		if char not in "aoyeui":
			result += "." + char
	return result


print stringTask()