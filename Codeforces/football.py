def football():
	userInput = raw_input()
	if "0000000" in userInput or "1111111" in userInput:
		return "YES"
	else:
		return "NO"


print football();


