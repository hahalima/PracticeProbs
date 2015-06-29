def binary2int(n):
	num = n.split(",")
	int_num = [x for x in num if int(x, 2)&5 == 0]
	return ",".join(int_num)

def B2Iconcise(n):
	return ".".join([x for x in n.split(",") if int(x,2)%5 == 0])

print binary2int("0100,0011,1010,1001")
print B2Iconcise("0100,0011,1010,1001")