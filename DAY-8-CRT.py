'''
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number

# Eg : 3
#def profile(name,age,place):
#    print(name, age, place)
#profile("sid", 29, "cbe")

#def profile(name, age, place):
#    txt = "my name is {}. iam {} years old. iam from {}."
#    print(txt.format(name, age, place))
#profile("sid", 29, "cbe")

# Eg : 4
#---> Function with return statement

# return
#1.) A value declared inside the function can be accessed outside the funtion using return
#2.) return does not print anything
#3.) we cannot write ant code below return statement
#def f1():
#    z = 8
#f1()
#print(Z)  # --> error - cannot use outside the function

#def f1(a, b):
#    c = a*b
#    return c
#print(f1(6, 8))
#obj = f1(6, 8)
#obj1 = f1(4,6)

#def gracemark(object):
#    print(object+4)
#gracemark(obj)    #==> 53
#gracemark(obj1)   # ==> 28


#123  ----> write polydrome code  pb - 1

# problem:1
# 123
# def palindrome(n):
#     string = str(n)
#     rev = str(n)[::-1]
#     if string==rev:
#         print(n, "palindrome")
#     else:
#         print("Not palinddrome")
# a = int(input("Enter the value: "))
# palindrome(a)


#Based on the declerartion of parameters and argd
#functions are devided into 5 catagories

#Positional args
#keyword args
#default args
#variable length args
#keyword variable length args

# ---> Positional args

#Eg:1
#def profile (name, phone, mark):
#    txt ="My name is {}. My phone number is {}. I got {} marks."
#    print(txt.format(name, phone, mark))
    
#profile (9878776767, "sidhu", 97)  # unexpected error

# ---> keyword args
# eg :1
# --> to overcome the disadvantage of position, we use keywor args
# --> it is the process of initialising the parameter with the args while  calling the function

#def profile(name, phone, mark):
#    txt = "My name is {}. My phone number is {}. I got {} marks."
#    print(txt.format(name, phone, mark))
    
#profile(name="sid", mark=96, phone=1234567890)

# ---> Execption of keyword args Function

#def profile(name, phone, mark):
#    txt = "My name is {}. My phone number is {}. I got {} marks."
#    print(txt.format(name, phone, mark))

#profile(name="adarsha", 1234456788, mark= 98) #--> error - positional args followed keyword args
#profile(1234456788, name="adarsha", mark=98)  # --> error - name has multiple vales
#profile("adarsha", mark=98, phone=123456788)

# ---> Default args
# -- The method of assiging the argument to the parameter while declaring the function
# Eg ; 1
#def profile(name, phone, place = 'pkd'):
#    txt = "My name is {}. My phone number is {}. I am from {}."
#    print(txt.format(name, phone, place))

#profile("adarsha", 99392979454)
#profile("adarsha", 99392979454, "kadapa")

# Ex : 2
#def profile(name, phone, place = 'pkd'):
#    txt = "My name is {}. My phone number is {}. I am from {}."
#    if  place != "pkd":
#        print("your not eligible")
#    else:
#       print("you are eligible")
#    print(txt.format(name, phone, place))

#profile("adarsha", 99392979454, "pkd")

# ---> Exception

#def profile(name, place = 'pkd', phone):  # error - coz defalut args should not follow positional param
#    txt = "My name is {}. My phone number is {}. I am from {}."
#    if  place != "pkd":
#        print("your not eligible")
#    else:
#       print("you are eligible")
#    print(txt.format(name, phone, place))

#profile("adarsha", 99392979454)


# ----> Variable length parameters
# Eg:1

#def profile(*name):
#    print("my name is",name)
#profile("adarsha", "upi", "somu") # ===> my name is ('adarsha', 'upi', 'somu')


# --> to pass more than 1 arg to a parameter means we use variable length args
#name = 'adarsha','upi','somu'
#def profile(*name):
#    for val in name:
#        print("my name is",val)
#profile("adarsha", "upi", "somu")

                    # my name is adarsha
                    # my name is upi
                    # my name is somu

# Eg :2

#def profile (*name, age):
#    for val in name:
#        print("My name is", val, "may age is", age)
#profile("sid", 'name2', 'name3', 28) #error-> age has no args

#def profile(age, *name):
#    for val in name:
#        print("My name is", val, "may age is", age)
#profile(28, "sid", 'name2', 'name3')

# ----> keyword variable length args
# Eg:1

#def price(**price_list):
#    print(price_list)

#price(shirt=1000, iphone=80000)

#n = 5
#{1:1, 2:4, 3:9, 4:16, 5:25}

#n = int(input("Enter the number: "))
#d1 = {}
#for val in range(1, n+1):
#    d1[val] = val**2
#print(d1)

#def dict1(n):
#    d1 = {}
#    for val in range(1, n+1):
#        d1[val] = val**2
#    print(d1)
#dict1(5)

'''
# ----> Object Oriented Programming

#The paradigms of objects oriented progarmming are

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ----> Class is a blue print of an object 
# l1 = [1,2,3,4,5,6]

# Eg:1

#class c1:
#    name1= "adarsha"
#    print(name1)

# Eg:2

#class person:
#    name = "adarsha"

#c = person()# c is object
# The process of creatio of an object is called as instantiation
#print(c.name)

# Eg:3

# create a method
# When the function is created with a class is called as method

# --> method without parameter
#class person:
#    def display(person):  # it is a method
#        print("hello welcome to class")

#p = person()
#p.display()

# Eg:4
#----> Method with parameter
#class person:
#    def display(person,name,age):
#        print(name, age)

#p = person()
#p.display("sidhu", 28)

# Ex:5
#class person1:
#    fname = "Adarsha"  # attribute or static variable
#    lname = "K"
    
#    def first_name(self):
#        print(self.fname)

#    def full_name(self):
#        print(self.fname+" "+self.lname)

#p = person1()
#p.first_name()
#p.full_name()


# Eg:6
# ---> Constructor ===> __init__()

#-----> This is a special method which has the ability to excute itself  withot calling it manuallly through the process of instantiation

#class profile:
#    def __init__(self): # --> constructor method
#        print("hey")

#p = profile()  #---> Excution of constructor through this process 
#p.__init__()




















































