def factorial (n):
	result = 1
	while n>0:
		result = result * n
		n = n-1
	return result  
prompt = raw_input("Enter a number that you want to get the factorial for: ")
print factorial(int(prompt))