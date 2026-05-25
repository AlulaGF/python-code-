#Search numbers to manupulat matimatics
import re
hand = input("Please Enter file name: ")
data = open(hand,'r' , encoding = 'utf-8')
content = data.read()
sumlist=[]
count = 0
for line in data:
	line = line.rstrip()
	line = line.split()
	num = re.findall('[0-9]+', line)
	for nums in num:
		sumlist = sum(sumlist)
		count = num + 1
print("Sum:",sumlist)
print("Count:", count)
		
