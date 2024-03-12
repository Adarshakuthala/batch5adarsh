#a=7, 8
#print(a)
#print(type(a))

#  a, b, c = 9, 8, 7, 8
# print(a,b,c)

#a,b=c=7, 8
#print(a)
#print(b)
#print(c)

#a=b, c =4, 2
#print(a, b, c)

# --->Swapping of Variables
#a = 7
#b = 5

#temp=a
#a=b
#b=temp
#print(a, b)

#Eg:2

#a=a+b
#b=a-b
#a=a-b

#print(a, b)
'''
a, b=b, a # only in python
print(a, b)
'''

#a=a*b
#b=a/b
#a=a/b

#print(a,b)

#---> id function id()
#------ Which is used to find the memory of the variable
#a=7
#b=8
#print(id(a))
#print(id(b))

#----> Keywords
#--- Keywords are reserved words which provides special meaning to
#    compiler or interpretor


#import keyword
#print(keyword.kwlist)
#print(len(keyword.kwlist))
#print(type(keyword.kwlist))

#---> to check if the string is keyword or not
#print(keyword.iskeyword("sid")) #false

#if = 8
#print(if)  #error coz is is a keyword

#!----> Literals
# literl is the constant value assigned to a variable
# A variable is considers to be constant whrn it is defines in caps

# a= 78 ==> a is variable
# A= 78 ==> A is constant

#-----> hash()==> it create a hash value for constant datatypes and provides error for non constant datatypes
#n1 = 89+7j
#print(hash(n1)) ==>7000110

#f1 = [7, 8, 9]
#print(hash(f1)) ==>TypeError: unhashable type: 'list'

#!---->  Operators
#==> operators are synbols which is used to perform various operations b/w 2 or more operations

# Arithematic
# Assignment
# logical
# Relational or comparison
# Bitwise
# Identify
# Membership

#==> Arithematic --> +, -, *, /, %, //,**
#Eg:1
# a = 8
# b = 6
# c = 9
# print(a+b+c+)

# input() --> used to get the runtime input
#---> eval()-- used to get the runtime values of all of all datatype

#n1 = input("Enter the value:")
#print(n1)

#a = 4
#b = 2
# print(a/b) # is used to grt the quotient value
# print(a%b) # used to get the reminder value

# // --> floor division operator
#a = 765433
#b =19

#print(a/b)
#print(a//b) --> the output will be inn integer & the output will be based on the floor

# **  ----> used for power of a number
# print(2**4) ---> 16

# Assignment Operators --->  =, +=, -=, /=, //=, **=, &=, |=

# a=8
# a+=2
# print(a) --> 10

#a=30
#a-=5
#print(a) --> 25

# Comparision --> ==, >, <, !=, <=, >=
#a=8
#b=7
#print(a>b) --> True
#a=9
#b=5
#print(a==b)

# Bitwise Operator --> &, |, ~, <<, >>
#a=7
#b=4
#print(a&b)

# 2^4 2^3 2^2 2^1 2^0
# 8   4    2   1

# 0   1   1   1   ---> 7
# 0   1   0   0   ---> 4 &
# -------------------
# 0   1   0   0

# ~ -->
#a=5
#print(~a)  --> -6 next -ve value 

# <<, >>
#print(5<<3)

# Logical operator
# and, or, not
#a = 6
#print(a>3 and a<10)---. true
#print(a>7 or a<30)
#print(not(a>8 and a<10)) ---> convert false into true and true into false

# identify oprators
# is, is not
#a = 8
#b = 8
#print(a is b)
#print(a==b)
#print(a is not b)

# Membership Operator
# in, not in
# 11 = [7, 8, 9, 0, 6, 5]
#num=55
#print(num in 11) ---> false
#print(num not i 11) --> true

#num = 678
#print(8 in num) --> error

# Conditional statement
#if, elif, else

#Eg-1:
# a = 6
#if a:
#    print("hello")


#Eg:2
#a = 6
#if a>3:
#    print("hey")
#else:
#    print("no")

#Eg:3
#if 7>8:
#    print("hello")

#Eg:4
#a = 0
#a = None
#a=False
#a=""
#if a:
#    print("yes")
#else:
#    print("no")

# a number is even or odd
#n = int(input("enter the number: "))
#if n %2==0:
#    print(n, "is even")
#else:
#    print(n, "is odd")

# name, age, nationality
# 18 above, indian
name = input("enter the name")
age = int(input("enter the age"))
nationality =input("enter the nation")

if age >=18 and nationality=="Indian":
    print("eligible for vote")
else:
    print("not eligible")


























