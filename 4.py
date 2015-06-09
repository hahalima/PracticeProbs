def tupleList():
	# get input from the user
	input = raw_input()
	# use the split() method to make the string to list
	inputList = input.split()
	# convert the list into a tuple
	inputTuple = tuple(inputList)
	print inputList
	print inputTuple

tupleList()