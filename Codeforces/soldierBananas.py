def soldierBananas():
	userInput = [int(x) for x in raw_input().split()]
	k = userInput[0]
	n = userInput[1]
	w = userInput[2]
	moneyNeeded = 0
	for i in range(1,w+1):
		moneyNeeded += i * k
	return moneyNeeded-n
print soldierBananas()