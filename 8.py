def alphabetically(n):
	items = n.split(',')
	items = sorted(items)
	return ','.join(items)

print alphabetically("without,hello,bag,world")