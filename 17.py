def bankAccount():
	total = 0
	while True:
		input = raw_input()
		if input == "":
			break;
		else:
			input = input.split(" ")
			print input

			if input[0] == "D":
				total = total + int(input[1])
			elif input[0] == "W":
				total = total - int(input[1])
	return total

print bankAccount()
