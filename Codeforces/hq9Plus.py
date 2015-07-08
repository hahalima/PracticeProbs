def hq9Plus():
	userInput = raw_input()
	if "H" in userInput or "Q" in userInput or "9" in userInput:
		return "YES"
	else:
		return "NO"
print hq9Plus()