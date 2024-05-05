print("SquareRoot.py is running...")
import math as m 
import time as t 
from collections import Counter
import numpy as np
usingNum = 0
objNum = 0
factorList = []
orList = []
def main():
	In = input('Enter Number: ')
	start_time = t.time()
	In = In.replace(" " , "")
	if In == 'exit':
		return
	if In == 'quit':
		return
	try:
		InNum = int(In)
	except:
		print("Only enter postive real numbers!")
	PNLIST = primeNumbers(InNum)
	functionRoot(InNum,PNLIST)
	end_time = t.time()
	print(f"Finished running loop in {end_time - start_time:.2f} seconds.")
	print('type "exit" or "quit" to quit program.')
	main()
def primeNumbers(x):
	print("PrimeNumbers.py is running...")
	output = [2]
	down = 3 #DO NOT INCLUDE 1 OR 2
	up = x #input -> variable in implementation
	def prime(n):
		if n <= 1:
			return False
		for i in range (2 , int(np.sqrt(n)) + 1):
			if n % i == 0:
				return False
		return True
	for n in range(down,up + 1):
		if prime(n):
			output.append(n)
	output.append('end')
	return output
def endFact(num,objNum,PNLIST):
	if num != 1:
		fact(num ,0,PNLIST)
	else:
		factorList.append(1)
		factorList.sort()
		print('Factors:',factorList)
		res = [(key, key) for key, val in Counter(factorList).items()
								for _ in range(val // 2)]
		for obj in res:
			orList.append(res[objNum][0])
			factorList.remove(res[objNum][0])
			factorList.remove(res[objNum][1])
			objNum += 1
		print('Factor Square Root:' , multiplyList(orList) , '√(' , multiplyList(factorList) , ')')
		print("-----------------------")
		factorList.clear()
		orList.clear()
def fact(num,usingNum,PNLIST):
	if num == 1:
		return
	if PNLIST[usingNum] == 'end':
		endFact(num,0,PNLIST)
	else:
		if num % PNLIST[usingNum] == 0:
			factorList.append(PNLIST[usingNum]) 
			num = num / PNLIST[usingNum]
			usingNum += 1
			fact(num,usingNum,PNLIST)
		else:
			usingNum += 1
			fact(num,usingNum,PNLIST)
def functionRoot(number,PNLIST):
	print("Absolute root: √(" , number , ') = ' , m.sqrt(number))
	orgNum = number 
	usingNum = 0
	fact(number,0,PNLIST)
def multiplyList(mypList): 
    result = 1
    for x in mypList:
         result = result * x
    return result
main()
