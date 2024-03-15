# ---> common functions for list

# l1 = [6, 7, 8, 9, 0]

# print(len(l1))  ==> 5

# print(max(l1)) ==> 9

# print(min(l1)) ==> 0

# l1 = [6, 8, 9, 'r', 'u']
# print(max(l1)) ==>  not supported between instances of 'str' and 'int'
# print(min(l1)) ==>  not supported between instances of 'str' and 'int'

# l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# print(min(l1)) ==> -5

# l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
# index() --> to get index value of specific element
# print(l1.index(9)) ==> 3

# l1 = [6,6,6,7,8,9,0,8.89,-5,0.79]
# count() --> how many num of times an element is repeated
# print(l1.count(6)) ==> 3

# Some functions which is specifically used for list

# to add element inside list
# insert(index_value, element) --> to add element at specific index position
# l1 = [6,6,6,7,8,9,0,8.89,-5,0.79]
# l1.insert(2,"cars")
# print(l1)  ==> [6, 6, 'cars', 6, 7, 8, 9, 0, 8.89, -5, 0.79]

#  to delete element from list
# l1 = [6,6,6,7,8,9,0,8.89,-5,0.79]
# pop() ---> last element will be deleted
# l1.pop()
# print(l1) => [6, 6, 6, 7, 8, 9, 0, 8.89, -5]

# l1.pop(4)
# print(l1) ==> [6, 6, 6, 7, 9, 0, 8.89, -5, 0.79]

# romove(element) --> used to delete element directly
# l1.remove(8.89)
# print(l1) ==> 8.89 will be removed from list

# clar() --> to complete delete all element in list
# l1.clear()
# print(l1)  ==> []


# del --> to complete delete all list
# del 11 or del (11)
# print(11)
# -----> join 2 lists

#l1 = [9, 0, 8]
#l2 = ['f','d','e',87]
#print(l1+l2)   # ---> [9, 0, 8, 'f', 'd', 'e', 87]

# or
# extend() ---> to combine 2 lists
# l1.extend(12)
# print(l1)  #--->   [9, 0, 8, 'f', 'd', 'e', 87]

# ----> copy()

#l1 = [6,7,8,9,3]
#l2 = l1.copy()
#print(l2)
#print(l1)

#print(id(l2))
#print(id(l1))

#-----> diff b/w shallow copy and deep copy
#--> shallow copy

#import copy
#l1= [8,9,0,[5,6],[3,2,1]]
#l2 = copy.copy(l1)
#print(l1)
#print(l2)    # ---> [8, 9, 0, [5, 6], [3, 2, 1]]
#                    [8, 9, 0, [5, 6], [3, 2, 1]]


#import copy
#l1= [8,9,0,[5,6],[3,2,1]]
#l2 = copy.copy(l1)
#l1.append(890)
#print(l1)
#print(l2)    # ---> [8, 9, 0, [5, 6], [3, 2, 1], 890]
#                    [8, 9, 0, [5, 6], [3, 2, 1]]


# ---> deep copy

#import copy
#l1 = [8,9,0,[5,6],[3,2,1]]
#print(l1[-1][1]) #---> to index nested list

#l2 = copy.deepcopy(l1)
#l1[-1].append('cars')
#print(l1)
#print(l2)  # -----> [8, 9, 0, [5, 6], [3, 2, 1, 'cars']]
#                    [8, 9, 0, [5, 6], [3, 2, 1]]

# ------> sort - arrange elements in list in ascending or descending order

#l1 = [9,7,45,0,-6,5,12]
#l1.sort()  # --> arrange in ascending order
#print(l1)  # ---> [-6, 0, 5, 7, 9, 12, 45]

#l1.sort(reverse=True)
#print(l1)   # -- > [45, 12, 9, 7, 5, 0, -6]

# ---> list constructor
# list --> to convert other collections data type to list

#l3 = ((8,9,0))
#print(list(l3))


# ----> nested list

#l1 = [8,9,[0,8,7],['p','o','y'],[8,'t']]
#print(l1[-2][1]) ==> o

#print(l1[1:4])    #---> [9, [0, 8, 7], ['p', 'o', 'y']]
#print(l1[1:-1])   #---> [9, [0, 8, 7], ['p', 'o', 'y']]

# to  delete  "t" from l1

#l1 = [8,9,[0,8,7],['p','o','y'],[8,'t']]
#l1[-1].remove('t')
#print(l1)    # ---> [8, 9, [0, 8, 7], ['p', 'o', 'y'], [8]]

# combine these ['p','o','y'],[8,'t'] list in l1 to ['p','o','y',8,'t']

#l1 = [8,9,[0,8,7],['p','o','y'],[8,'t']]
#l1[-2].extend(l1[-1])
#l1.pop(-1)
#print(l1)   # ---> [8, 9, [0, 8, 7], ['p', 'o', 'y', 8, 't']]

# ---> Tuple
# char of tuple

# 1. tuple have to be sorrounded by ()
# 2. the elements inside the tuple are not changable
# 3. the elements inside tuple indexed
# 4. the element will excute in order
# 5. it allow duplicate elements


#eg;1
#t1 = (8,8,9,6,5.78,[9,0],(6,8),"hey", 9+6j)
#print(t1)
#print(type(t1)) # ----> <class 'tuple'>

# indexing, slicing are all same as list

#l1 = [8]
#print(type(l1))   #  --->  <class 'list'>

#l1 = (8)
#print(type(l1))   # ---> <class 'int'>

#l1 = (8,) # and 8,9
#print(type(l1))    # ---> <class 'tuple'>

'''
len(), min(),max(),index(),count() ---> all same as list
'''

# to add element inside tuple --> cannot add
# cannot delete any element from tuple

# jion 2 tuples
#t1 = (8,9,0)
#t2 = (6,7,8)
#print(t1+t2)  ----> (8, 9, 0, 6, 7, 8)

# to add all element inside list and tuple
#sum()
#l1 = (8,9,7,6,)
#print(sum(l1))  ===> 30

# --> sort tuple
#t1 = (8,9,0,89,12)
#print(tuple(sorted(t1)))    #  ---> (0, 8, 9, 12, 89)
#print(tuple(sorted(t1, reverse=True)))   3 ---> (89, 12, 9, 8, 0)

# iterate list and tuple

#l1 = [9,8,0,6,5]
#for i in l1:
#    print(i)    #----> 9
#                       8
 #                      0
  #                     6
   #                    5


# iterare based on index value

#l1 = [9,8,0,6,5]
#for i in range(0,5):
#    print(l1)      #  -----> [9, 8, 0, 6, 5]
#                             [9, 8, 0, 6, 5]
#                             [9, 8, 0, 6, 5]
#                             [9, 8, 0, 6, 5]
#                             [9, 8, 0, 6, 5]


#print(l1[2])


#l1 = [9,8,0,6,5,8,56]
#for i in range(0,len(l1)):
#    print(l1[i])

# ------> Strings

#s1 = "o"
#print(type(s1))  # ----> <class 'str'>

#s1 = 'u'
#print(type(s1))

#s1 = "hello world"
# To access string
#print(s1)
# indexing and slicing ----> same as list and tuple

#print(s1[0:8])   # -----> hello wo

# ------> common functions in string
# len(), min(), max(), index(), count()

#s1 = "hello world"
#print(len(s1)) ------>11
#print(max(s1)) ------>w
#print(min(s1))  ----->

# ord() ---> use to find the ASCII value of character
#s1 = 'u'
#print(ord(s1))    # ----> 117

# functions of string
#s1 = 'hello world'

# to convert all characters to upper case
#print(s1.upper())

# to convert lower case
#s1 = "ADARSHA"
#print(s1.lower())

# --> strip() --> to elimate the space in beginning and end of the string
#s1 = " Where are you?"
#print(s1.lstrip())
#print(s1.rstrip())
#print(s1.strip())

# split()--> to split the words in string based ona character
#s1 = "where are you?"
#print(s1.split())
#print(s1.split("r"))


# ---> replace()
#s1 = "where are you?"
#print(s1.replace('r', '@'))

# ----> swapchcase()---> to convert capital to small and small to capital at a time
#s1 = "HEY there"
#print(s1.swapcase())

# --> title() --> to write string in format of title
#s1 = 'never giveUP'
#print(s1.title())

# --> capitalize()----> 1st char of string will be convertd to capital
#s1 = 'never giveUP'
#print(s1.capitalize())

#--> jion the strings
#s1 = 'hello'
#s2 = 'world'
#print(s1+s2)

# splitline() --> used to split the string based on lines
#s1 = '''
#how are you
#iam fine
#hey there
#'''
#print(s1.splitlines())   #---> ['', 'how are you', 'iam fine', 'hey there']

# find() ---> to find the index based on the character
#s1 = "hello world"
#print(s1.find('h'))
#print(s1.index('z'))

# --> join()-->
#l1 = ["hey", "there"]
#print(" ".join(l1))
#print("&".join(l1))

#s1 = "welcome to all"
#print(s1.endswith('l'))
#print(s1.startswith('l'))

#s1 = "67"
#print(type(s1))
#print(s1.isdigit())

# --> print the string in reverse manner
#s1 = "welcome to all"
#print(s1[::])
#print(s1[::-1])

# Eg;1
# wap to find the number of lowercase
#s1 = " HEY there you aRE"
#count = 0
#for i in s1:
#    if i.islower():
#        count+=1
#print("the total number of lowercase letters: ",count)

# ---Eg;2  r----> "$"
#s1 = 'restarter'
#fst=s1[0]
#bal=s1[1:]
#txt=bal.replace(fst,"$")
#print(fst+txt)    #resta$te$

# Eg;3

#s1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
#characters=(len(s1))
#print(characters)

#words = s1.split(" ")
#print(len(words))

#s1= s1.strip()
#sentenses = s1.split('.')
#for val in sentenses:
#    if val =='':
#        index = sentenses.index('')
#        sentenses.pop(index)
#print(len(sentenses))

#space = 0
#for val in s1:
#    if val ==" ":
#        space=space+1
#print(space)
