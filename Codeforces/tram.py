def tram():
	numberOfTimes = int(raw_input())
	maxPeople = 0;
	tempPeople = 0
	while numberOfTimes>0:
		n,k = map(int, raw_input().split())
		tempPeople -= n
		tempPeople += k
		if (tempPeople > maxPeople):
			maxPeople = tempPeople
		numberOfTimes -= 1
	return maxPeople

print tram()
