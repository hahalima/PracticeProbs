class prob5:
	def __init__ (self) :
		self.string = ""
	def getString(self):
		self.string = raw_input()
	def printString(self):
		print self.string.upper()

A = prob5()
A.getString()
A.printString()