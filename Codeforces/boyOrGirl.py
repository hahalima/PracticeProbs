def boyOrGirl():
	userInput = raw_input()
	userSet = set(userInput)
	if len(userSet)%2 == 0:
		return "CHAT WITH HER!"
	else:
		return "IGNORE HIM!"

print boyOrGirl()