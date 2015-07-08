def builtInFunctions(num):
	"""Test the abs(), int(), and raw_input() documentations through __doc__
	Prints stuff out """
	print "Absolute value of " + str(num) + " is: " + str(abs(num))
	print "Integer value of " + str(num) + " is: " + str(int(num))
	print "Your raw input is: " + raw_input()
	print abs.__doc__
	print int.__doc__
	print raw_input.__doc__


builtInFunctions(5.0)
print builtInFunctions.__doc__