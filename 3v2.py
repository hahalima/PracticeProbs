def num_dict(number):
	temp = {}
	for i in range(1,number+1):
		temp[i] = i * i
	return temp

print num_dict(8)