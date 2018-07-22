def fibb(n):
	result = None
	if n < 0:
		print("You are trying to cheat me! Game over, you're done!")
	elif n == 0:
		result = 0
	elif n == 1:
		result = 1
	else:
		result = fibb(n-1)+ fibb(n-2)
	return result

def Main():
	print("I'm going to print fibbonacci and factorial calculation results")
	print(fibb(-6))
	
if __name__ == "__main__":
	Main()
