import time

def calc_square(numbers):
	print("Calculate square numbers")

	for n in numbers:
		time.sleep(0.2)
		print('square: ', n*n)

def calc_cube(numbers):
	print("Calculate cube of numbers")
	for n in numbers:
		time.sleep(0.2)
		print('cube: ', n*n*n)

arr = [5,4,3,2,1]

calc_square(arr)
calc_cube(arr)

t = time.time()

print("USE TIME = ", t)



