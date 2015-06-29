def evens():
	result = []
	for num in range(1000, 3001):
		temp = num
		while temp > 0:
			if (temp%2 == 0):
				temp = temp/10
			else:
				break;
		if temp == 0:
			result.append(str(num))
	return ",".join(result)

print evens()