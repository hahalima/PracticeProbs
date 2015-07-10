def translation():
	s = raw_input()
	t = raw_input()
	reverse_s = ""
	for char in s:
		reverse_s = char + reverse_s
	if reverse_s == t:
		return "YES"
	else:
		return "NO"

print translation()
