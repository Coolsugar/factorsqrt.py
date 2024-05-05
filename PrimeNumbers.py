print("Print PrimeNumbers.py is starting...")
import time as t
import numpy as np
print('Imports completed...') 
output = [2]
down = 3 #DO NOT INCLUDE 1 OR 2
up = int(input("Select upper limit: ")) #input -> variable in implementation
def prime(n):
	if n <= 1:
		return False
	for i in range (2 , int(np.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True
print("Functions defined...")
start_time = t.time()
print("Running...")
for n in range(down,up + 1):
	if prime(n):
		output.append(n)
end_time = t.time()		
print(output)
print(f"Finished running loop in {end_time - start_time:.2f} seconds.")