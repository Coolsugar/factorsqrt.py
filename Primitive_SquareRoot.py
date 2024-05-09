print("Square root any number you want!")
import math as m 
import time 
from collections import Counter
usingNum = 0
objNum = 0
factorList = []
orList = []
prmNum = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 'end' ]
print('Imported math modules.')
def end():
	print('Program Ended')
def rawRoot():
	pass
def multiplyList(mypList): 
    result = 1
    for x in mypList:
         result = result * x
    return result
def endFact(num,objNum):
	if num != 1:
		fact(num , 0)
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
def functionInput(redo):
		if redo == 1 :
			print('To end the program type "exit" or "quit".')
			numberInput = input('Enter Number: ')
		else:
			numberInput = input('Enter Number: ')
		numberInput = numberInput.replace(" " , "")
		if numberInput == 'exit':
			end()
		elif numberInput == 'quit':
			end()
		else:
			try:
				num = int(numberInput)
				functionRoot(num)
			except:
				print('Please enter a numerical value only!')
				functionInput(0)
def fact(num,usingNum):
	if prmNum[usingNum] == 'end':
		endFact(num,0)
	else:
		if num % prmNum[usingNum] == 0:
			factorList.append(prmNum[usingNum]) 
			num = num / prmNum[usingNum]
			usingNum += 1
			fact(num,usingNum)
		else:
			usingNum += 1
			fact(num,usingNum)
def functionRoot(number):
	print("Absolute root: √(" , number , ') = ' , m.sqrt(number))
	orgNum = number 
	usingNum = 0
	factorList = []
	fact(number,0)
	functionInput(1)
functionInput(0)