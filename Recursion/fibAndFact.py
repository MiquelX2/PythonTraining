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
		result = fibbRecursive(n-1)+ fibbRecursive(n-2)
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
def fibbIterative(n):
	result = None
	if n<0:
		print("Game over!")
	elif n == 0:
		result = 0
	elif n == 1:
		result = 1
	else:
		previous = 1
		previousButOne = 0
		for i in range(2,n+1):
			result = previous + previousButOne
			if i<n:
				previousButOne = previous
				previous = result
	return result
def Main():
	print("I'm going to print fibbonacci and factorial calculation results")
	print(fibbRecursive(200))
	print(fibbIterative(200))
	
if __name__ == "__main__":
	Main()
