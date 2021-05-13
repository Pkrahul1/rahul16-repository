
class Product:
    pass
p1=Product()
p1.price=10; #setting attribute only for this object , ths feature only available in python.
class Student:
    def __init__(self):
        self.address="chapra"
        self.__age=23#this wont be accesible outside class ,encapsulation..2 but actually change the name for outside class 
        print("in constructor")
    def printName(self):#one agr is mandatory , 1st is always ref of object , standard practice is self.
        print("rahul age:{} address:{}".format(self.__age,self.address))
    def __str__(self):
        return "you are in str"
s1=Student()
s1.printName()#above and this both do the same. 2.To invoke method we dont need to know the details of method, abstraction
s1.address="patna" #price can be changed as it's public
#print(s1.__age)#will give arror as s1.__age is not accessible outside Student' object has no attribute '__age'
s1.__age=24#will not give error but create a attribute with this name 
print(s1._Student__age)# 23 as __age is changed to _Student__age for outside class
s1.printName()
s1._Student__age=25#this willl change the __age attribute for the object.
s1.printName()
print(s1)#to print customised output use __str__ inbuilt method
print("...use getter setter to access __age from outside...")

class Product:
    def __init__(self ,name, mob):# this is called aggregation, when object is passed in one of the method its not agg, weaker reln.
        self.name=name            # when object of a class is created in method of another class then also no aggr,weaker reln
        self.mob=mob # mob is object of Mobile class 
    def description(self):
        print("name is {} , price is {},version is {}".format(self.name,self.mob.get_price(),self.mob.get_version()))

class Mobile:
    discount=20#static variable accessed across instance variable,should be accessed using class name
    __version=2.1
    counter=1000
    def __init__(self,price):
        self.__price=price
        Mobile.counter+=1
    def set_price(self,price):
        self.__price= self.__price if price <= self.__price else price
    def get_price(self):
        return self.__price
    def purchase(self):
        print("price is {}".format(self.__price-(Mobile.discount*self.__price)/100))
    @staticmethod
    def get_version():#no self required , can be accessed without creating object
        #print(self.__price) #will give error as self is unknown here, only static variable and method can be accessed from
        return Mobile.__version# from static method
    @staticmethod
    def set_version(version):
        Mobile.__version=version
    def __str__(self):
        return str(self.__dict__)
m1=Mobile(10000)
m1.set_price(9000)
#print(m1.get_price())#10000
m1.set_price(11000)
#print(m1.get_price())#11000 
#print(m1.purchase())
Mobile.discount=10#if discount is private use getter setter
#print(m1.purchase())
print(Mobile.get_version())
Mobile.set_version(3.1)
#print(Mobile.get_version())
print(m1)# using __str__ , it ll print attributes and values in dictionary for the onject
#p1=Product("Nokia 6.1 Plus",m1)
#p1.description()
print(".........inheritance.......")
"""
child can inherit constructor , methods and attribute. private attribute cant be accessed directly , need to use getter
setter from child class. if child has no constructor ,parent contructor will be called if it has ,parent constructor wont
be called , same rule for methods.to explicitly call parent methods and constructor use super().__init__(name,price) or 
super().Methodname(),self not passed. this is overriding of parent method. if child has own constructor and not used super
to call parent constructor it wont inherit parent attribute also.
"""
class Product:
    def __init__(self,name):
        print('inside product constructor')
        self.name=name
    def feature(self):
        print("name:")
class Mobile(Product):
    def __init__(self,name,os):
        self.os=os
      #  print(self.name)# will give error as parent constructor not called.
#m1=Mobile("SmartPhone","andriod")
#m1.feature()#call parent feature
#print(m1.name)#will give error as mobile object didn't go to parent constructor
#print(m1.os)#wont give error

class Mobile1(Product):
    def __init__(self,n,os):   
        print("inside mobile constructor")
        super().__init__(n)
        self.os=os
    def feature(self):
        super().feature()
        print("name:{} OS:{}".format(self.name,self.os))
m1=Mobile1("SmartPhone","andriod")
m1.feature()#call child feature
#print(m1.name)
#print(m1.os)
print(".......multilevel inheritance............")
"""if child object created it will search for constructor in child first if not found will go parent if not will go to
grand parent..in case of multiple inheritance it will go according to the order of parent inherited.
"""
class GrandParent:
    def __init__(self):
        print("in grand parent")
    def print_name(self):
        print("print name in grand parent")
class Parent(GrandParent):
    pass
class Child(Parent):
    pass
c1=Child()
c1.print_name()
print(".....multiple inheritance....")
'''
creting object will start searching for constructor from 1st inherited parent used. if gets a particular method it will use
that methos only even if another inherited parent have same method with same or different signature. construtor overloding 
is not available in python.same rule for method or constructor.
'''
class Parent2:
    def __init__(self):#def __init__(self,name): using this signature also call init of Child only when creating obj of
        print("in parent 2")#grandchild because 
    def print_name(self):
        print("printing name in Parent2 :")
    def print_your_name(self,name):
        print("you name in parent2: %s"%(name))
class GrandChild(Child,Parent2):
    pass
gch=GrandChild()#start from child before parent2 as child is 1st inherited class, will go till all child parent are over
#gch.print_name()
#gch.print_your_name("rahul")#this method not found in Child or in child's parents.so parent2 is used.
print("......abstract classand method........")
"""
abstract class shouldnt be instanciated even if instanciated wont give error. but if abstract clas have abstract method it 
cant be instanciated. abstract class can have both abstract and not abstract methods. child sud must override abstract method 
if not overring it also becomes abstract class so its instance can be created.
if a child class overrides abstract method then its own child need not to override the abstract method.
"""
from abc import ABCMeta,abstractmethod
class MyParent(metaclass=ABCMeta):
    def __init__(self):
        print("in myparent")
#mp1=MyParent()#instanciated even if abstract class

class MyParent1(metaclass=ABCMeta):
    def __init__(self):
        print("in myparent")
    @abstractmethod
    def print_name(self):
        print("abstract method can also be implemeted in abstracted class unlike in C#")#
    def fun(self):
        print("this is not abstract but defined in abstract class")
#mp1=MyParent1()#will give error cant be instanciated
class MyChild(MyParent1):
    pass
#mc=MyChild()#will give error as not overriden
class MyClass1(MyParent1):
    def print_name(self):#overriding parent abstract method
        print("printing name in mychild1")
        super().print_name()#calling abstract method of abstract class
        self.fun()#calling on abstract method of abstract class

mc2=MyClass1()
#mc2.print_name()
#mc2.fun()
print("..................................................................")
print("...........Custome iteratoro..........")
# Python code showing use of iter() using OOPs 

