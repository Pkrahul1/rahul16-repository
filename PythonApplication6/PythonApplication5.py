import time
import operator
import string
import random
import itertools # works on iterator to produce complex iterator next works on produced,
                 # list tuple dict are iterable , con using iter to apply next
from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
#print(end="@")   
#print(end=" ")
#print(end="")
#print(end=" ")
# Python code showing use of iter() using OOPs 


list1=[1,2,3,4]
list2=[5,6,7,8]
i=10
print("...........infinite iterators.........")
a = itertools.count(5,2) #infinitely from 5 with step 2 , can be used in for loop
a=itertools.cycle(list1) # infinitely in the iterable, 
a= itertools.repeat(i,5)# 5 is optional repeat i 5 times else infinitly
a= product([1,2],[3,4])# object but iterator not iterable ,return cartisiion product.
print(a)
print(list(product([1,2],repeat=4))) # repeat is optional 
print(".....permutation and combination......")
print(permutations([1,2]))
print(permutations([1,2,3],2))# 2 is optional , in gropu of 2
print(combinations([1,2,3],2))# 2 is not optional
print(combinations_with_replacement([1,2,3],2))# 2 is not optional
print("..........Accumulate and star mapsimilar to map.. ")
print(list(itertools.accumulate([1,2,3,4,5],operator.mul)))#2nd arug is optional, by default add , sim to map
print(tuple(itertools.accumulate([1,2,3,4,5])))
print("sliced: ",list(itertools.islice([10,20,30,40,50,60,70,80,90],2,8,2)))#start stop step
print("......filter and false filte..............")
print(list(itertools.filterfalse(lambda x:x%2==0 ,[1,2,3,4,5,6,8])))# gives value for false
print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7])))
print("..........chain and others iterators.. ")
print(list(itertools.chain(list1,list2)))
print(list(itertools.compress([1,2,3,4,5],[True,False,True,False,True])))#from 2nd list sect which to slkt from 1st lst
print(list(itertools.dropwhile(lambda x:x%2==0 ,[2,4,6,7,9,8,10])))#pritn all elements in list after 1st time false met
print(list(itertools.takewhile(lambda x:x%2==0,[2,4,6,7,9,8,10])))#print all elements in list brfore 1st time false is met
print("......tee.........")
print(itertools.tee(iter(list1),3))
print(list(itertools.tee(iter(list1),3)))
iteronj=itertools.tee((list1),3)
for i in range(len(iteronj)):
    print(list(iteronj[i]))
print(list(itertools.zip_longest([1,2,3,4,5],["rahul","kumar","singh"],fillvalue="not given")))#shorte is filled with fillvalue if exhausted


list1=[0,1,2,3,4]
list2=[10,20,30,40,50]
list3=map(lambda x:x**2, list1) #map or any itertools return iterator but list is itrbl.
print(next(list3))
print(next(list3))
print(next(list3))
print(next(list3))

t1=time.time()
for i in range(5):
    print(list1[i]*list2[i],end=" ")
t2=time.time()
print("time in normal: ",t2-t1)
t1=time.time()
r1,r2,r3,r4,r5=map(operator.mul,list1,list2)
t2=time.time()
print(r1,r2,r3,r4,r5)
print('time in map: ',t2-t1)

l1=[1,2,3]
l2=["rahul","kumar","singh"]
t1=(10,20,30)
print(".....ZIP......")
print(zip(l1,l2))#l2 can be tuple or any iterator
n=zip(l1,l2)#its iterator till shortest.
print("next:",next(n))
print(list(zip(l1,l2)))
for i in zip(l1,l2):
    print(i,type(i))
for a, b in zip(l1,l2):
    print(a,b,end="\n")
print("...UnZipp.........")
a,b= zip(*[(1,"rahul"),(2,"singh")])#unboxing operator first removes list and  makes tuples which is zipped.
print("1.",a,b)                 #zip(*((1,"rahul"),(2,"singh"))) same with this.
x=list(zip(l1,l2))
print("2.",x)
print("3.",[zip(l1,l2)])#line 88 and 90 is not same
a,b=zip(*x)
print("4.","a,b in after unzip:",a,b,sep="   ")
x=zip(l1,l2)
for i in zip(*x):
    print(i,type(i),"unzipping")

X = [[1,2,3],
    [4 ,5,6],
    [7 ,8,9]]
print("5.",list(zip(*X)))
print("6.",list(map(list,zip(*X))))
for i in zip(*X):
    print("7.",i)
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]] 
result= zip(*([1,2,3],[9,8,7])) #((1,2,3),(4,5,6)) 
for i in result:
    print("8.",i)
print("......enumerate......")
print(enumerate(l2,10))
print(list(enumerate(l2,10)))
for i in enumerate(l2,10):
    print(i)
for a, b in enumerate(l2,10):
    print(a,b,end="\n")

"""
i=0
while(i<2):
    print(i)
    i=+1
    if(i==1):
        break;#else only executed if break never executes no no error in while loop same for for loop
else:
    print("outside")

l1=[1,2]
l2=iter(l1)
print(next(l2))
print(range(10),type(range(10)))

for i in range(4):
    print(i,end='>>')
    print(time.clock())
   
a,b=1,10
#print(a>b?a:b) not used in python
#number= 20 if a>b else 10 
print(number)
'''rahul 
kumar'''
#obove is multiline comment
number= int(input())
print(number)
print("my name is {} {}".format("rahulk","singh"))
print("my name is {0} {1}".format("rahulk","singh"))
print("my name is {1} {0}".format("rahulk","singh"))
print("age d is for integer 2 for precision %2d , decimal 5 is prcision including . %5.2f" %(10,06.233))
l1=[1,2,3,4,0,False,True]
print(any(l1),all(l1))#any true check all check all true 
l2=[]
print(any(l2), all(l2))
"""