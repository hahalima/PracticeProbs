def petyaStrings():
	string1 = raw_input().lower()
	string2 = raw_input().lower()
	if string1<string2:
		return -1
	elif string1>string2:
		return 1
	else:
		return 0

print petyaStrings()