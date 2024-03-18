# ----> Assesment
# 1.)Merge two python dictionary
#d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#d1.update(d2)
#print(d1)
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

#set1 = {'Python', 'Java', 'Data Science'}
#set2 = {'ML', 'AI', 'R Language', 'Python'}
#set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}

#c = 0
#flag = 0
#for val in range(3):
#    c=c+1
#    if c==1:
#        for val in set1:
#            if val in set2 or val in set3:
#                flag=1
#                break
#    if c==2:
#        for val in  set2:
#            if val in set1 or val in set3:
#                flag=1
#                break

#    if c==3:
#        for val in  set3:
#            if val in set2 or val in set1:
#                flag=1
#                break
#if flag==0:
#    print("Disjoint")
#else:
#    print("joint")

    

# 3.)
#list1 = ["M", "na", "i", "Ke"]
#list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']

#l3 = []
#for val in range(len(list1)):
#    ans = list1[val]+list2[val]
#    l3.append(ans)
#print(l3)    

#i = 0
#l3 = []
#while i<len(list1):
#    l3.append(list1[i]+list2[i])
#    i+=1
#print(l3)

# ----> Functions

# --> Function is a block of code which is used to perform a specific functionality
# ---> Functions can be created using def keyword

# --> Function has 3 parts
#1. Function declaration
#2. Function defanatiion
#3. Function call

# -> eg :1
#def greet(): # --> Function defination
#    print("Greeetings User!!")
#greet()
#greet()  # --> function calling

# eg : 2
#def adding():
#    a= 8
#    b= 6
#    c= 5
#    d= a+b+c
#    print(d)
#adding()
#adding()

#def greeting(name):
#    print("welcome", name)
#greeting("Upi")
#greeting("Adarsha")


#def greeting(name):
#    print("welcome", name)
#for val in range(3):
#    username = input("Enter the name: ")
#    greeting(username)


# Eg : 3
#def profile(name,age,place):
#    print(name, age, place)
#profile("sid", 29, "cbe")



# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number




















































