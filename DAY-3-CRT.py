# EG: 3
# take value of lenth and breadth of a from user and check if it is square or not

#length = int(input())
#breadth = int(input())
#if length==breadth:
#    print("its a square")
#else:
#    print("its not square")

# Eg:4
# Python program to check wheather the given ineteger is multiple of both 5 and 7

#n= int(input("enter the number: "))
#if n%5==0 and n%7==0:
#    print("yes")
#else:
#    print("no")

# Eg:5
# Write the program to accepth the cost price of a bike and display the road tax to be paid
# according to the following criteria :

#   Cost price (in price)                               Tax
#   >100000                                             15 % + discount 6%
#   >50000 and <= 100000                                10%
#   <= 50000                                            5%

#price = int(input("enter the price: "))
#total = 0
#if price>=100000:
#    discount = price*(6/100)
#    value = price-discount
#    tax = value*(15/100)
#    total=value+tax
#else:
#    tax = price*(5/100)
#    total = price + tax
#print("the on road cost of bike is: ",total)
'''
# if elif statement
# Eg:1
a = 55
b = 9
c = 3

if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else: #or
#elif c>a and c>b:
    print("C is greater")

# A school has following rules for grading system:
# a. below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 t0 80 - B
# f. above 80 - A
# Ask user to enter marks and print the corresponding grade.

mark = int(input("enter mark: "))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("Fail")
'''

# ----> short hand if else
#Eg: 1
#a=9
#b=65
#if a>b:
#    print("A")
#else:
#    print("B")
# ----> using short hand if else
# -----> Rules
# 1. Statement inside the if condition have to be present at  first
# 2. elif cannot be used in shor hand if else
# 3. always it have to end with else

#print("A") if a>b else print("B")

#code to check the given char is vowel or consonent

#char = input("Enter the char: ")
#if char=="a" or char=='e' or char=='i' or char=='o' or char=='u':
#    print("is a vowel")
#else:
#    print("its consonent")

# or

#strl = "aeiouAEIOU"
#if char in strl:
#    print("vowel")
#else:
#    print("consonent")

#char = input("Enter the char: ")
#strl = "aeiouAEIOU"
#print("vowel") if char in strl else print("consonent")

# ----> elif ladder using short hand if else
#Eg : 1
# Find greatest among 3 variables using short hand if else
#a=8
#b=6
#c=5

#print("A is greater") if a>b and a>c else print("B is greater") if b>a and b>c else print("C is greater")


# -------> looping
# looping can be implemented using
# for loop
# while loop

# -----> for loop
#  for loop is used for iteration, if we know the number of times the loop have to run
#  it is used to iterate the iterables eg(string, list, tuple, etc...)

# ---> syntax for loop

# for syntax in c
#for(i=0;i<10;i++){
#   printf("hello");
#}

#--> for syntax in python

#for userdefined_variable in range(start, end, step): default step value is 1
#    statement
#    statement
#    statement

#Eg : 1
# to print the value from 1 to 10 using for loop

#for i in range(0, 10): #(n, n-1)
#   print(i)


# EG : 2
#for val in range(23, 87, 3,):
#    print(val)

# Eg : 3
# to decrement the value

#for val in range(10, 0, -1):
#    print(val)

# Eg : 4
# print the output of 7th multiplication table from 21 to 43

#for val in range(1, 10):
#   print(val*7)

#----> Method 1
#for val in range(1, 10+1):
#    print('7','x',val,'=',val*7)

#----> Method 2
#for val in range(1,11):
#    ans="7 x {} = {}"
#    print(ans.format(val,val*7))

#----> Method 3
#for val in range(1,11):
#    print(f"7 x {val} = {val*7}")


# Eg : 5
# break --> usedto terminate the loop

#for val in range(1, 10):
#    if val ==6:
#        break
#    print(val)

# Eg : 6
#for val in range(1, 10):
#    print(val)
#    if val ==6:
#        break


#for val in range(1, 10):
#    if val ==6:
#        print(val)
#        break


# ---> continue
#Eg :1
#for val in range(1,20):
#    if val == 6:
#        continue
#   elif val == 15:
#        continue
#    print(val)


#for val in range(1,20):
#    if val == 6 or val == 11 or val ==19:
#        continue
#    print(val)
    

# -----> Pracrice problem
# print the even numbers between 20 t0 40

#for val in range(20, 41):
#    if val %2==0:
#        print(val)

# print the 0dd numbers between 20 t0 40

#for val in range(20, 41):
#    if val %2!=0:
#        print(val)

#for loop practice
# write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

#for val in range(12, 37+1):
#    if val %2!=0:
#        print("odd numbers: ",val)
#    elif val %2==0:
#        print("even numbers: ",val)




#-------> while loop
# whike is used when we do not know the number of times the loop have to ron
# to iterate the non iterable elements while loop is used

#--> syntax
#initialisation
#while condition:
#    statement
#    incre or decre

# Eg : 1
# tp iterate number from 1 to 10

#i = 0
#while i<11:
#    print(i)
#    i+=1 # or i=i+1

# Eg : 2
#10,1
#i = 10
#while i>0:
#    print(i)
#    i=i-1






















































