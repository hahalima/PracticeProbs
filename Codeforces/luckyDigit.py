def luckyDigit():
	userInput = raw_input()
	count = 0
	for char in userInput:
		if char=="4" or char=="7":
			count += 1
	if count==int("4") or count==int("7"):
		return "YES"
	else:
		return "NO"

print luckyDigit()