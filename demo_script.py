#!/bin/python3
#this script makes use of different loops such as while, for loop and if... else decision making statement
yes=input("enter 1 or 0: ")
#if...else
if int(yes):
	print("welcome to new session")
	name=input("enter your name: ")
	print("Hi ",name)
else:
	print("your session got expired")
	print("Thank you")

a=20
b=20
#checks whether two variables points to same object
if(a is b):
	print("a is identity to b")
else:
	print("a is not identty to b")


li=[56,57,6,8,69]
#checks whether the given element is member of list
if(56 in li):
	print("it is a member of list")
else:
	print("it is not a member of list")
	
#while loop
tot=0
i=0
#iterates through list for adding the elements in list
while(i<len(li)):
	tot+=li[i]
	i+=1
print(tot)	

#for loop
list1=[ ]
#converting each element in given list to complex data type
for i in li:
	list1.append(complex(i,1))

print(list1)

#block of code which tells whether given number is prime or not
num=int(input("enter a number"))

if(num%2==0):
	print("the given number is even")
else:
	i=3
	flag=0
	while(i<=num):
		if(num%i==0):
			flag=1
		if(flag==0):
			print("the given number is prime")
			break
		i+=1
	




	


