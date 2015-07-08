def georgeAccomodation():
	numRooms = int(raw_input())
	roomsAvailable = 0
	while numRooms > 0:
		peopleInRoom, roomCapacity = map(int, raw_input().split())
		if roomCapacity - peopleInRoom >= 2:
			roomsAvailable += 1
		numRooms -= 1
	return roomsAvailable

print georgeAccomodation()
