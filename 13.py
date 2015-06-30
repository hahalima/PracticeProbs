def calcDigitsLetters(n):
	num_letters = 0
	num_digits = 0
	for char in n:
		if char.isdigit():
			num_digits+=1
		elif char.isalpha():
			num_letters+=1
	print "LETTERS " + str(num_letters)
	print "DIGITS " + str(num_digits)

	
calcDigitsLetters("hello world! 123")