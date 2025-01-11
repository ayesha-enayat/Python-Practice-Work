name="Ayesha"
fName="Enayat"
#Strings can be concatenated using the + operator
print(name+ " " + fName)

#Strings can be repeated using the * operator
print(name*3)

#length of str
print("length of name: ",len(name))

#Indexing in python
print(name[0])
#name[0]='B' not allowed


#Slicing in python
#str[starting_index: ending_index] ending _index is exclusive
str="ApnaCollege"
print(str[0:4]) #prints Apn
print(str[:4])
print(str[1:])

#Negative Slicing
str1="Apple"
print(str1[-3:-1]) 

#strings Functions
str2="i am a coder"
print(str2.capitalize()) #first letter of string is capital
print(str2.upper()) #all letters of string are capital
print(str2.lower()) #all letters of string are small
print(str2.count('am')) #count of a in string
print(str2.find('a')) #index of a in string
print(str2.replace('a','b')) #replace a with b in string
print(str2.endswith("er")) #check if string ends with er


#conditional statement
num = int(input("Enter your number: "))
if (num % 2 == 0):
    print("Num is even")
else :
    print("Num is odd")



marks = int(input("Enter your marks: "))
if (marks >= 90):
    print("Grade A")
elif (marks >= 80 and marks < 90):
    print("Grade B")
elif (marks >= 70 and marks < 80):
    print("Grade C")
elif (marks >= 60 and marks < 70):
    print("Grade D")
else:
    print("Fail")







