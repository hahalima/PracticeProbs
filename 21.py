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
			if direction == "UP":
				y = y + movement
			elif direction == "DOWN":
				y = y - movement
			elif direction == "LEFT":
				x = x - movement
			elif direction == "RIGHT":
				x = x + movement
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
			direction = input[0]
			movement = int(input[1])
			if direction == "UP":
				position[1] = position[1] + movement
			elif direction == "DOWN":
				position[1] = position[1] - movement
			elif direction == "LEFT":
				position[0] = position[0] - movement
			elif direction == "RIGHT":	
				position[0] = position[0] + movement
			else:
				pass
	return int(round((math.sqrt(position[0]**2 + position[1]**2))))


print robotStepsv2()