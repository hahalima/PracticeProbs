def factorial(n):
	result = 1;
	#print range(1,n)
	for i in range(1, n+1):
		result = result * i
	return result

prompt = raw_input("Enter a number that you want to get the factorial for: ")
print factorial(int(prompt))
