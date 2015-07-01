import math
def robotSteps():
	result = 0
	x = 0
	y = 0
	while True:
		input = raw_input()
		if input == "":
			break
		else:
			input = input.split(" ")
			if input[0] == "UP":
				y = y + int(input[1])
			elif input[0] == "DOWN":
				y = y - int(input[1])
			elif input[0] == "LEFT":
				x = x - int(input[1])
			elif input[0] == "RIGHT":
				x = x + int(input[1])
	result = math.sqrt(x*x+y*y)
	return round(int(result))

def robotStepsv2():
	position = [0,0]
	while True:
		input = raw_input()
		if input == "":
			break
		else:
			input = input.split(" ")
			if input[0] == "UP":
				position[1] = position[1] + int(input[1])
				print position[1]
			elif input[0] == "DOWN":
				position[1] = position[1] - int(input[1])
			elif input[0] == "LEFT":
				position[0] = position[0] - int(input[1])
			elif input[0] == "RIGHT":	
				position[0] = position[0] + int(input[1])
	return int(round((math.sqrt(position[0]**2 + position[1]**2))))


print robotStepsv2()