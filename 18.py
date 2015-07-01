import re
def validPassword(n):
	passwords = n.split(",")
	result = []
	for word in passwords:
		if (re.search('\w', word) and re.search(r'[$#@]', word) and len(word) >=6 and len(word)<=12):
			result.append(word)
	return ",".join(result)


print validPassword("ABd1234@1,a F1#,2w3E*,2We3345, adfaFDA5432")
