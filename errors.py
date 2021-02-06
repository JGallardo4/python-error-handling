# Shows the uses of try-except-else-finally

# Division by zero
try:
	result = 10 / 0
except ZeroDivisionError:
	print("10 / 0: You cannot divide by zero")		
else:
	print("10 / 0: No exceptions raised")
finally:
	print("10 / 0: This code always runs\n")
  
# No error
try:
	result = 10 / 2
except ZeroDivisionError:
	print("10 / 2: You cannot divide by zero")		
else:
	print("10 / 2: No exceptions raised") # Note that else runs when no exceptions are raised
finally:
	print("10 / 2: This code always runs\n")

# This is how we can catch any error
try:
	raise SystemError("SystemError1")
except ZeroDivisionError:
	print("SystemError1: You cannot divide by zero")
except BaseException as err:
	print("SystemError1: There was some error")		
	print(err)
	pass
else:
	print("SystemError1: No exceptions raised")
finally:
	print("SystemError1: This code always runs\n")

# System error is not being handled by our code
try:
	raise SystemError("SystemError2")
except ZeroDivisionError:
	print("SystemError2: You cannot divide by zero")	
else:
	print("SystemError2: No exceptions raised")
finally:
	print("SystemError2: This code always runs\n")