def stonesOnTable():
	numStones = int(raw_input())
	stoneColors = raw_input()
	count = 0
	for stone in range(0,numStones-1):
		if stoneColors[stone:stone+2] == "RR" or stoneColors[stone:stone+2] == "BB" or stoneColors[stone:stone+2] == "GG":
			count += 1
	return count

print stonesOnTable()