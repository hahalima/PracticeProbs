def capitalize():
	temp = []
	while (True):
		text = raw_input("enter text (type in yes or no to stop): ")
		if text == "yes" or text == "no":
			break;
		else:
			temp.append(text.upper())
	for line in temp:
		print line


capitalize()