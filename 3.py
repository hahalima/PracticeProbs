def dictionary (n): 
	d = dict()
	for i in range(1,n+1):
		d[i] = i*i
	return d
print dictionary(8)