import math
def fibbRecursive(n):
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
def factorialRecursive(n):
	result = None
	if n<0:
		print("You're trying to cheat me! That's enough, game over!")
	elif n < 2:
		result = 1
	else:
		result = n*factorialRecursive(n-1)
	return result
def factorialIterative(n):
	result = 1
	for i in range(1,n+1):
		result *= i
	return result

def Main():
	print("I'm going to print fibbonacci and factorial calculation results")
	print(math.factorial(997))
	print(factorialIterative(997))
	print(factorialRecursive(997))
	
if __name__ == "__main__":
	Main()
