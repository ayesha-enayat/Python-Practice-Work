# Print Statement
print("Hello World!")
print(23)
print("My name is Ayesha","I am 0 years old")
print(35+5)
print(20-2)

#Variables
name="Ayesha Enayat"
print(name)
age=1
print(age)
price=25.88
print(price)
print("My name is: ",name)
print("My age is: ",age)

age2=age
print(age2)

#Rules for Identifiers
#1. It must start with a letter or underscore
#2. It can only contain letters, digits, and underscores
#3. It cannot start with a digit
#4. It cannot contain spaces
#5. It cannot contain special characters
#6. It is case sensitive
#7. It cannot be a keyword
#8. It cannot be a reserved word


#DataTypes
#Integer (+ve,-ve,0)
#Float  (9.6,2.2)
#string ('s',"s","'s'")
#Boolean (True or False)
#None (a=none)
print(type(name))
print(type(age))
print(type(price))


old=False
a=None
print(type(old))
print(type(a))


#keywords
#and,as,assert,async,await,break,class,continue,def,del, and so on


#Sum of two numbers
a=1
b=2
sum=a+b
print(sum)


#single line comment
"""
Multi line 
comments
"""


#Types Of Operators
#Arithmetic Operator (+,-,*,/,%,**)
#Assignment Operator (=,+=,-=,*=,/=,%=,**=)
#Comparison Operator (==,!=,>,<,>=,<=)
#Logical Operator (and,or,not)
c=5
d=5
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c%d)
print(c**d)

num1=50
num2=50
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)

num=10
#num=num+20
num += 10
print("num :" , num)

print(not False)
print(not True)
print(not (a>b))

val1=True
val2=False
print("And Operator: " ,val1 and val2)
print("OR operator: " ,val1 or val2)


#Type Conversion
#Type Conversion python ka interpreter humare liye automatically khud kardeta hai
#Type Casting manually type ko convert karna

k=2
l=4.25
print(k+l)

m="2"
n=3.2
print((int(m)+n))


x=3.14
y=str(x)
print(type(x),type(y))


#Input in Python
name6=input("Enter your name: ")
print("welcome ",name6)


val6=int(input("Enter val: "))
print("Entered ",val6) 
print(type(val6))
