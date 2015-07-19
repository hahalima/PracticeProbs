# def generalArrival():
# 	numSoldiers = int(raw_input())
# 	lineSoldiers = [int(num) for num in raw_input().split()]
# 	tallest = lineSoldiers[0]
# 	shortest = lineSoldiers[0]
# 	tallestPos = 0
# 	shortestPos = 0
# 	if (lineSoldiers.index(max(lineSoldiers)) == len(lineSoldiers)-1 and lineSoldiers.index(min(lineSoldiers)) == 0):
# 		return 0;
# 	for soldier in range(numSoldiers):
# 		if lineSoldiers[soldier] > tallest:
# 			tallest = lineSoldiers[soldier]
# 			tallestPos = soldier
# 		if lineSoldiers[soldier] <= shortest:
# 			shortest = lineSoldiers[soldier]
# 			shortestPos = soldier 
# 	print shortestPos, tallestPos
# 	if (lineSoldiers.index(tallest) < lineSoldiers.index(shortest)):
# 		return tallestPos + (numSoldiers - shortestPos+1)
# 	else:
# 		return tallestPos + (numSoldiers - shortestPos)-1

# def generalArrival():
# 	numSoldiers = int(raw_input)
# 	lineSoldiers = [int(num) for num in raw_input().split()]
# 	while lineSoldiers[0] != max(lineSoldiers) and lineSoldiers[len(lineSoldiers)-1] != min(lineSoldiers):
# 		if (lineSoldiers[0] != max(lineSoldiers)):
def generalArrival():
	numSoldiers = int(raw_input())
	tallest = 0
	shortest = 0
	lineSoldiers = [int(num) for num in raw_input().split()]
	for soldier in lineSoldiers:
		if soldier == max(lineSoldiers):
			tallest = lineSoldiers.index(soldier)
			break
	for soldier in range(numSoldiers-1, 0, -1):
		if lineSoldiers[soldier] == min(lineSoldiers):
			shortest = (numSoldiers-1)-lineSoldiers.index(lineSoldiers[soldier])
			break
	return tallest + shortest


print generalArrival()