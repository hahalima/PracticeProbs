def nyCandles():
	a,b = map(int, raw_input().split())
	hours = a
	while a >= b:
		newCandles = a/b
		a = newCandles + a%b
		hours += newCandles
	return hours

print nyCandles()