import time
import threading

def calc_square(numbers):
	print("quare numbers Func")

	for n in numbers:
		time.sleep(0.2)
		print('square : ', n*n)

def calc_cube(numbers):
	print("cube of numbers Func ")
	for n in numbers:
		time.sleep(0.2)
		print('cube: ', n*n*n)

arr = [5,4,3,2,1]

t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()

t2.start()

t1.join()

t2.join()

print("USE TIME = ", time.time()-t)



