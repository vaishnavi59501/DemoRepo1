#!/bin/python3
import sys

#variable
#name=input("Enter you name: ")
# sys module helps in accessing command line arguments into the script
'''len(sys.argv) returns the no of arguments including script and
 sys.argv returns the arguments in list  '''

print(len(sys.argv))
print(sys.argv)

print("Hi ",sys.argv[1]) #sys.argv[0] returns the script name, actual arguments start at index 1

eng,maths,sci=45,56,57 #multiple assignments in single line
tot_mark=eng+maths+sci

print(tot_mark)

a,b,c=int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])
print(a+b+c)


#string manipulation

sentence="how are you"

print(sentence[0]) #accessig first charter in string sentence using slice of operator
print(sentence[:7]) #accessing range of characters using [:]
print(sentence[2:]) 
print(sentence*4) #displaying sentence four times with repetition operator(*)
print(sentence +" hope doing well") #concatenating with another string

print(sentence[:4]+"do you do") #updating existing string at index four
print("%s"%sentence) #%s is the string format specifier to print the sentence
print(r"C:\\nowhere") #r denotes raw string this helps to suppress the actual meaning of escape character and gets it displayed like normal string, r should be given in preceding to the quotation

# triple quotes can be used for spanning string at multiple lines like a paragraph
para="""this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up."""

print("%s"%para)


#string functions
print(sentence.capitalize()) #capitalize() method displays the string with first character in upper case 

print(sentence.center(20,' ')) #centre() method displays by centering the string by padding with ' '

print(sentence.count('o',1,12)) #count() method counts the occurence of substring in given range of string sentence

new_sentence=sentence.encode('UTF-8','strict')
print(new_sentence.decode('UTF-8','strict')) #decode() method displays the original string by decoding the encoded string 

print(sentence.endswith("ow",1,3)) #endswith() method returns true if the specified substring is the suffix of the given range of characters in original string otherwise false

string="this is long\tgap"

print(string.expandtabs(16)) #expandtabs() method can be used to change the tabsize of \t 

print(sentence.find("are",2,8)) #find() method returns the index of found substring in original string

Str="this@123456"
print(Str.isalnum()) #isalnum() method returns true if the string contains alphabet and numbers otherwise false

print(sentence.isalpha()) #isalpha() method returns true if the string contains only alphabets otherwise false

Str="12345678"
print(Str.isnumeric()) #isnumeric() method returns true if the stirng contains only numbers otherwise false

print(sentence.swapcase()) #swapcase() method returns the string in opposite case (e.g. if string is in upper case it will be displayed in lower case or vice versa

print(sentence.islower()) #islower() method returns true if string is in lower case or false

Str="00000000hello everyone000000000"
print(Str.strip('0')) #strip() method performs both lstrip and rstrip i.e truncating leading and trailing padded filler character (say for example filler char '0'
print(Str.lstrip('0')) #lstrip() method removes leading filler char
print(Str.rstrip('0')) #rstruo() method removes trailing filler char

print(len(sentence)) #len() method returns the no of characters in the string

print(sentence.replace("are","old are")) #replace() method finds the old string and replaces it with new string

