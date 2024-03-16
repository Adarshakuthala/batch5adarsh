# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

#----> Q1
#s1 = 'never giveup'
#print(s1.capitalize())
#print(s1.replace('n','N'))
#print(s1.replace('p','P'))

#s1 = input("enter string: ")
#fst = s1[0].upper()
#lst = s1[-1].upper()
#print(fst+s1[1:len(s1)-1]+lst)

#---->Q2
#
#n = 128
#temp = n
#f1 = 0
#while n!=0:
#    rem = n%10
#    check = temp%rem
#    if check != 0:
#        f1= 1
#    n = n//10
#if f1==0:
#    print("yes")
#else:
#    print("no")


#----> Q3

#l1 = [8,9,0,7]
#l2 = [7,6,5,4]

#print(l1[0]+l2[0], l1[1]+l2[1])

#l3=[]
#for val in range(len(l1)):
#    ans = l1[val]+l2[val]
#    l3.append(ans)
#print(l3)


#-----> set

#---> charctristics of sets
#1. set can be created using {}
#2. the elements inside set are not indexed
#3. does not allow duplicate values
#4. it unordered
#5. heterogenous
#6. mutable or changable

#s1 = {9,9,89,7.76, 8+7j, (8,7,5),"truck",'e'}
#print(s1)

# eg; 2
#s2= {5,8,98,[9,0]}
#print(s2)----> error

# eg ; 3
#min(), max(), len()

#eg
# ---> to add element

#add()

#s1 = {8,78,67,'u'}
#s1.add(55)
#print(s1)

# update()
#s1.update([9,0])
#print(s1)

#  ---> to delete element inside set
#s1= {8,78,67,'u'}
#pop()---> to delete onelement randomly
#s1.pop()
#print(s1)

#remove()
#s1.remove(67)
#print(s1)

#discard()
#s1.discard(67)
#print(s1)

# clear()
# l1 = []
# print(type(l1)) --> datatype is dict

# s1 = set() # to create empty set
# print(type(s1))

# s1 = {8,9,0}
# s1.clear()
# print(s1)

# del s1
# print(s1)

# join the sets
# s1 = {9,0,8}
# s2 = {9.90,"card",'t',55}
# union() --> To combine 2 sets
# s3 = s1.union(s2)
# print(s3)

# intersection() --> To get commeon elements inside set
# s1 = {4,5,6}
# s2 = {5,6,7,8}
# print(s1.intersection(s2))

# difference()
# s1 = {4,5,6}
# s2 = {5,6,7,8}
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1.symmetric_difference(s2))

# isdisjoit(),issubset(),issuperset()

#s1 = {8,9,0}
#s2 = {6,7,5,8,9,0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))

# -------> problem 1

#s1 = {1,2,3,4,5}
#s2 = {3,2,7,8,9}
#for val in s1:
#    if val in s2:
#        str1="its joint set"
#print(str1)


# -------> dictionary
# EG : 1
#d1 = {1:100, 'a':200, 4.5:'hello'}
#print(d1)
#print(len(d1))

# -----> charcterstics of dictionary
#1. have to be surrounded by {}
#2. it have to be in the form of key, value pair
#3. it is mutable
#4. duplicate keys are not allowed, duplicate values ae allowed
#5. it is unindexed
#6. it is ordered
#7. key does not allow mutable datatypes, values allow mutable datatype

#d1 = {1:100, 2:200, 3:300, 4:400}
# to access elements in dictionary
#print(d1)
#or
# to access the values, have to use key
#print(d1[1])  #0/p ---> 100

# some common functions
#len(), min,max()
#print(min(d1))
#print(max(d1))

#--> to find min, max based on values
#print(min(d1.values()))
#print(max(d1.values()))


#----> dictionary based functions
# to add element(key and valaue pair) in dict

#d1 = {1:100, 2:200, 3:300, 4:400}
#d1[5] = 500
#print(d1)

# ---> To replace the value in dictionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d1[2] = "mango"
#print(d1)

# ---> delete element from dictionary
#d1 = {1:100, 2:200, 3:300, 4:400}
# ---> popitem()  --> to delete last key value pair in dictionary
#d1.popitem()
#print(d1)

# pop()
#d1.pop(2)  #---> 2 is the key dictionary
#print(d1)

#clear(). del

#join 2 dictionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"appale", "b":"boy", "g":"game"}
#d1.update(d2)
#print(d1)

# get()
#d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1[3])
#print(d1.get(90)) #----> none

# ----> to print all the keys()
#d1 = {1:100, 2:200, 3:300, 4:400}
#print(d1.keys())  # ----> dict_keys([1, 2, 3, 4])
#print(type(d1.keys()))   #---> <class 'dict_keys'>

# ----> to print all the values
#print(d1.values())

# ----> iterating dictionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#for val in d1:
#    print(val)

#for val in d1.values():
#    print(val)

#for key, val in d1.items():
#    print(key, val)
    
# ----> problem : 1
#n = int(input("Enter the value: "))
#integer=[]
#float_value=[]
#string=[]
#for val in range(n):
#    value=eval(input("Enter the values: "))
#    if type(value)==int:
#        integer.append(value)
#    elif type(value) == float:
#        float_value.append(value)
#    elif type(value) == str:
#        string.append(value)
#    else:
#        print("please provide data in int, float,string")
#print(integer)
#print(float_value)
#print(string)

# ----> problem : 2

# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}

#set1 = {10, 20, 30, 40, 50}
#set2 = {30, 40, 50, 60, 70}
#print(set1.symmetric_difference(set2))

#set3=set()
#for val in set1:
#    if val not in set2:
#        set3.add(val)
#for val in set2:
#    if val not in set1:
#       set3.add(val)
#print(set3)

# ----> problem 3
l1 = [1,2,3,4]  #key
l2 = ['a', 'b', 'c', 'd']  # value

d1 = {}
for val in range(len(l1)):
    d1[l1[val]] = l2[val]
print(d1)


#1.) Swap elements in String list
#The original list is is: ['Gfg', 'is', 'best', 'for', 'Geeks']
#List after performing character swaps: ['efg', 'is', 'bGst', 'for', 'eGGks']




#mech_name = ["name1", "name2", "name3"]
#mech_age = [23,22,24]
#mech_mark = [89, 78, 60]
#mech_email = ["name1@gmail.com", "name2@gmail.com", "name3@gmail.com"]
 




