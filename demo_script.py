#!/bin/python3

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
if(a is b):
	print("a is identity to b")
else:
	print("a is not identty to b")


li=[56,57,6,8,69]

if(56 in li):
	print("it is a member of list")
else:
	print("it is not a member of list")
#while loop
tot=0
i=0
while(i<len(li)):
	tot+=li[i]
	i+=1
print(tot)	

#for loop
list1=[ ]
for i in li:
	list1.append(complex(i,1))

print(list1)

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
	




	


