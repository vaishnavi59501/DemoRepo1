#!/bin/python3
#this scipt file contains list,tuple,dictionary and implementation of functions on list,tuple and Dictionary

#list
#list is collection of objects of different types and it is enclosed in square brackets.
li=['physics', 'chemistry', 1997, 2000]

list3 = ["a", "b", "c", "d"]
print(li[1]) #accessing first element in list li

print(li) #diplaying the list li
 
print(li[:2]) #displaying range of elements in list

print(li*2) #displaying list li two times using repetition operator(*)

l=li+list3
print(l) #concatenating two lists and displaying it

#updating list
li[2]='physics'
print(li)

a=1997
print(a in li) #returns true if a is member of list otherwise false

print(len(li)) #returns the no of elements in list

print(max(list3)) #returns maximum element in list list3

print(min(list3)) #returns minimum element in list list3

list3=list3+["e","f"] #adding elements to the list
print(list3)

tuple1=(1,2,3,4,5)
print("tuple :",tuple1) #converting sequence of elements (e.g. tuple) to list
print("tuple converted to list ",list(tuple1))

print(list1.count(123)) #returns the number of occurence of the element in the list

print(list3)
del list3[3] #deletes the element at index 3 in list3
print(list3)


#tuple
#tuple is similar to list but the difference is elements are enclosed using braces () and here updating tuple is not valid action.
tup=(23,) #declaring tuple with single element along with character comma
print(tup)

print(tup+(34,36,37)) #adding elements to tuple

print(len(tup)) #returns the no of elements in tuple

print(tuple(li)) #converts list li to tuple


#Dictionary
#Dictionary is kind of hash table type whicl has key-value pairs
dict1={1:"apple",2:"orange"} #declaring dictionary with key:value pair, here key can be of numeral or string datatype

print(dict1)

print(dict1[2]) #getting the value of key 2

print(dict1.keys()) #extracting keys set from dictionary

print(dict1.values()) #extracting values set form dictionary

dict1[3]="grapes" #adding new key value pair

print(dict1)

#del dict1[3]

print(dict1[1])

print(len(dict1)) # returns the no of key-value pairs in dictionary dict1

print(str(dict1)) # displays dict1 in string representation

print(type(dict1)) # returns the type of dict1

dict2=dict1.copy() #copying dict1 to dict2

print(dict2)

dict3=dict.fromkeys(list3,"value") #converting list to dictionary with default value-"value"
print(dict3)

print(dict1.get(2)) #accessing value of key 2 in dictionary

print(dict1.get(4,"pears"))

print(dict1)

dic={4:"avacado"}
dict1.update(dic) #adding new key-value pair to existing dict1 by update() method

print(dict1)

