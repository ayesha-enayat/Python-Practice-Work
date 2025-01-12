#List in python
marks=[87,55,33,96,76]
student=["Ayesha",85,"Delhi"]
print(student[0])
print(marks[2])
print(len(student))

#List slicing
marks=[87,55,33,96,76]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

#list Methods
list=[2,1,3]
list.append(4)
print(list)
list.sort()
print(list)
list.reverse()
print(list)
list.insert(2,7)
print(list)
list.sort(reverse=True)
print(list)
list.remove(1)
print(list)
list.pop(3)
print(list)


#Tuples
tup=(87,55,33,96,76)
# tup[0]=43 #not allowed 
print(marks)

tup1=()
print(tup1)
tup2=(1,)
print(tup2)
tup3=(1,2,3)
print(tup3)

tup=(2,1,3,1)
print(tup.index(1))
print(tup.count(1))


#practice
#Write a program to enter user names of their 3 fav movies and stored them in a list
movie_List =[]
for i in range(3):
    user_Input= input("Enter your fav movie")
    if(i==3):
        break
    movie_List.append(user_Input)
    print(movie_List)

#WAP to check if a list contains a palindrome of elements 
list=[1,2,3,2,1]

