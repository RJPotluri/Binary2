import math
import time
print("[Base10 to Binary conversion]")
base10 = int(input("Enter a positive integer: "))
start = time.time()
current = base10
if base10 > 0:
	# default values of x (exponent) as 0 and create an empty list 
	x = 0
	list = []
	# identify the highest poweer of 2, x = length of number (list)
	# x - 1 = highest exponent
	# thus x = 7 means the highest value is 2**6 = 64
	"""while 2**x <= base10:
		x += 1"""
	x = math.floor(math.log(base10,2))+1

	#create a list with 0's as placeholders for length (x) of number
	while len(list)<x:
		list.append(0)
	#set the first 0 equal to 1 as it is the highest exponent
	list[0] = 1
	#set the current number to the original - the highest power value
	current = (base10 - 2**(x-1))
	#set list_length to x in order to reset x and use it again
	list_length = x
	x = 0
	#while the current value is not 0, find the next highest power
	#by adding 1 to x until 2**x is greater than the current value
	#at this point, subtract 1 to x to reduce it to the highest exponent
	while current > 0:
		while 2**x <= current:
			x += 1
		x -= 1
		#set the index of the appropriate exponent to 1
		list[((list_length-1)-x)] = 1
		#update the current value by subtracting the next highest power
		current = current - 2**x
		#reset x, start the loop again
		x = 0

	#convert the list of integers into a single string	
	string1 = ''.join(str(e) for e in list)
	print ()
	print("==============================")
	print("Converted:")
	print("FROM Decimal(Base10): %s" %(base10))
	print("  TO Binary (Base02): %s" %(string1))
	print("in %f seconds." % (time.time() - start))
	print("==============================")
elif base10 == 0:
	print ()
	print("==============================")
	print("Converted:")
	print("FROM Decimal(Base10): %s" %(base10))
	print("  TO Binary (Base02): 0")
	print("in %f seconds." % (time.time() - start))
	print("==============================")
else:
	print ("Number must be a positive integer or 0")