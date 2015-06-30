def oddOnly(n):
	seq = n.split(",")
	result = []
	for num in seq:
		if (int(num)%2 == 1):
			result.append(num)
	return ",".join(result)

print oddOnly("1,2,3,4,5,6,7,8,9")