def noDuplicates():
	input = raw_input().split()
	temp = []
	for i in range(0, len(input)):
		if input[i] not in temp:
			temp.append(input[i]) #this was the important line
	temp = sorted(temp) #remember that parameter for sorted() is lists, not strings
	return " ".join(temp)

def noDuplicatesV2():
	#input = raw_input().split()
	input = "hello world and practice makes perfect and hello world again".split()
	print input
	result = []
	return [x for x in input if x not in result]

def test():
	input = "hello world and practice makes perfect and hello world again".split()
	print input
	for i in input:
		print i
print noDuplicatesV2()
#print test()