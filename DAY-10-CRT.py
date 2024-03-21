#1----> Tasks

#Write the code for the below tasks using function
#1.) dl=("shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30)
#a.) Find the min ans max priced product
#b.) Find the product starts with 's' and 'S'

#2.) Find then 67, is strong number or not

#3.) 11 = [1,2,3,4,5,6]
#n=2> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]


# --> Method Over-riding
# - polymorphisam in classes using Inheritance

#class bank:
#    def ratio(self):
#        print("all banks has repo rate")

#class SBI(bank):
#    def ratio(self):
#        print("SBI ratio is 9%")

#class IOB(bank):
#    def ratio(self):
#        print("IOB rate is 7.5%")

#i = IOB()
#i.ratio()

#s = SBI()
#s.ratio()

# ? Eg:2
#class USA:
#    def langauge(self):
#        print("English")

#    def capital(self):
#        print("washington Dc")

#class India(USA):
#    def langauge(self):
#        print("None")

#    def capital(self):
#        print("New delhi")

#I = India()
#I.langauge()
#I.capital()

# ! Eg:3
#polymorphism using objects

#c1, c2, --> c1 = print(c1), print(c2)
#f1, f2

# eg:4
#class c1:
#    def f1(self):
#        print("class 1")

#class c2(c1):
#    def f1(self):
#        super().f1()
#        print("class 2")

#obj1 = c2()
#obj1.f1()

#obj2 = c2()
#obj2.f1()

#obj1=c2()
#obj2=c1()

#def display(a):
#    a.f1()
#display(obj1)
#display(obj2)

# ---> changing the functionality of builtin functions
#class shooping:
#    def item_list(self, l1):
#        items = len(l1)
#        print(items)

#s = shooping()
#print(s)    #-->  <__main__.shooping object at 0x0000024B98A5FA30>
#print(len(s))

#class shooping:
#    def __init__(self, l1):
#        self.items = l1

#    def __len__(self):
#        length = len(self.items)
#        return length
#s = shooping([1,2,3,4,5])
#print(len(s))

# ---> Method over loading
# Eg:1
#class summing:
#    def add(self, a, b):
#        print(a+b)
#        
#    def add(self, a, b, c):
#        print(a+b+c)

#s = summing()
#s.add(4,3) # --> error
#s.add(4, 5 , 1)
    
# ! Eg:2
#class summing:
#    def add(self, a=None, b=None, c=None):
#        if a!=None and b!=None and c!=None:
#            print(a+b+c)
#        elif a!=None and b!=None:
#            print(a+b)
#        else:
#            print(a)
#            
#obj= summing()
#obj.add(2)
#obj.add(3, 4)
#obj.add(1,2,3)

# ----> Abstraction
# The process of hiding the implementation details is abstraction

# Eg:1

#from abc import ABC,abstractmethod
#class shapes:
#    def sides(self):
#        print("All shapes have sides except circle")

#class triangle(shapes):
#    def traingle_sides(self):
#        print("3 sides")

#    def name(self):
#        print("Iam traingle")

#    def sides(self):
#        pass

#class square(shapes):
#    def square(self):
#        print("4 sides")

#tr = triangle()
#tr.traingle_sides()
#tr.name()

#! -----> Rules to define abstract class1

#1.) Abstract class cannot be instantiated
#2.) from abc import ABC, abstractmethod
#3.) subclass the normal class with ABC
#4.) convert the normal method inside the abstract class to abstract method
#5.) all the child classes have to be subclassed with abstract class
#6.) The abstract method should be present in the child classes

# Eg:2
#super()

#from abc import ABC,abstractmethod
#class c1(ABC):
#   @abstractmethod
#   def m1(self):
#      print("This is abstract class")
#      
#class c2(c1):
#   def m2(self):
#      super().m1()
#      print("Iam child 1")
#
#   def m1(self):
#      pass
#   
#class2 = c2()
#class2.m2()

# EG:3
#from abc import ABC, abstractmethod
#class password(ABC):
#   @abstractmethod
#   def pwd(self):
#      pswd = "somy25$"
#
#class login(password):
#   def validate(self, name, password):
#      if super().pwd() == password:
#         print("welcome", name, "!!")
#         print("login successfull")
#      else:
#         print("please check your password")

#   def pwd(self):
#      pass

#Login = login()
#name = input("enter the name: ")
#pwd = input("enter the passeord: ")
#Login.validate(name, pwd)


# ----> Encapsulation
# Eg:1
#class car:
#    __name = 'BMW'  # if we double underscore ( __ ) it will be private variable
#
#c1 = car()
#print(c1.name)
#c1.name = 'Audi'
#print(c1.name)

# Eg:2
# --> Accessing private date outside the class
#class c1:
#    __phone = '9392979454'
#
#    def display(self):
#        print(self.__phone)
#
#c = c1()
#c.display()

# ---> Eg:3
#--> declare private method

#class class1:
#    def __m1(self): # private method
#        print("iam private method")
#
#    def __init__(self):
#        self.__m1()
#
#c = class1()
#c.__m1()  # error


# --> nested class

#class class1:
#    class class2:
#        name = "Adarsha"
#
#        def display(self):
#            print(self.name)
#    obj1=class2()
#
#obj = class1()
#obj.obj1.display()

#!---->Tasks
# Write the code for the below tasks using function
#1.) d1 {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}

#d1 ={"shirt": 1000, "pant": 1500, "Shoes": 900, "handkey": 30}
#for val in d1:
#    if d1[val] == min(d1.values()):
#        print(val)
#for val in d1:
#    if d1[val] == max(d1.values()):
#        print(val)
#for val in d1:
#    if val.startswith('s') or val.startswith('S'):
#        print(val)






















































































