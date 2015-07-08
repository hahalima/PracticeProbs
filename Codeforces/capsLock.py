def capsLock():
	userInput = raw_input()
	if len(userInput) == 1:
		return userInput.upper()
	elif userInput[0].islower() and userInput[1:].isupper():
		return userInput[0].upper() + userInput[1:].lower()
	elif userInput.isupper():
		return userInput.lower()
	else:
		return userInput
print capsLock() 