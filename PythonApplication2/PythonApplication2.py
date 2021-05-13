from functools import reduce;
import os;
import operator

import operator
l1=[1,2,3,4]
l2=[10,20,30,40]
a,b,c,d=map(operator.mul,l1,l2)
#print(a,b,c,d) #unboxed to a b c d
a,b=range(2)
#print(a,b)

def gen1(n):
    i=10;
   
    yield i;
    yield 10;
    return 1;
    yield 10;
    return 1;

#b=iter(gen1(10));#gen fn is always iterator ,no need to convert excplicitly using iter 
#b=gen1(10) 
#print(next(b))
#print(next(b))
#print(next(b)) # this will give error
''' when 1st time next function is encountered gen will be executed till 1st yield
 and below that yield code wont be executed when 2nd next function encountered code will be 
 resumed from where it was left and will be executed till next yield is encountered
 again below code will be suspended. when next is executed for the third time there was no
 yield left and so it will give stopIteration Error'''   
'''so generator does not give complete data once at a time but its keeps on executing
inside generator function from 1st yield till last yield is encountered. if return statement 
is encountered it will come out of the generator right there and will give stopIteration
error incase further next function is encountered'''
def gen2(n):
    j=1;
    k=0
    for i in range(n):
        print("below yield is for: {} yield".format(j))
        j+=1
        yield i**2;
        k=10
#g1=gen2(10)
#print(g1)#g1 is iterator
#print(next(g1))
#print(next(g1))
#print((gen2(5))) #<generator object gen2 at 0x0000020EA56C6990>
#print(list(gen2(5)))#will give list of all yield but all print is also executed
##print(dict(gen2(5)))#will give error
#print(iter(gen2(5)))#<generator object gen2 at 0x0000020EA56C6990>
#print(list(iter(gen2(5))))#will give list of all yield but all print is also executed
#for element in gen2(5):
#    print(element)
'''inside for loop or in list() tuple() function generator object is automatically
converted to iterator no need to use iter or next'''

def gen(n):
    for i in range(n):
        yield i**3;

def advanceFunGenerator():
    #print(next(range(10))) # this  will give error
    print(range(10),type(range(10)),sep=":");
    print(list(range(1,8,2)))
    print(list(iter(range(1,8,2))))
    '''print(next(range(10))) #TypeError: 'range' object is not an iterator
    next function can be applied on iterator. only list dict set tuple string 
    all are iterable can be converted to iterator using iter() function and then next
    function can be applied in them.iter function can be applied on iterable only.
    for loop convert iterable to iterator internaly and iterate through iterable'''
    a=iter(range(10,100,5));
    print("\n1.................");
    for i in range(10):
        print(next(a),end=" ");
    print("\n2.................");
    '''generator:it will creat an object like range(n) which can be used in loop 
    but should be converted to iterator to call next function'''
    print(gen(10))#its an object <generator object gen at 0x00000176A9BB69E8>
    print(list(gen(10)))
    for i in gen(10):
        print(i,end=" ");
    print('\n3.....................');
    for i in range(10):
        print(next(gen(12)),end=" ")#will always give first element bcz calling different fn everytime , iter cn b usd as gen(12) is iterator 
    print("\n4.....................")
    v= iter(gen(12));
    u=gen(10)#it is also iterator
    print(v)#its an object <generator object gen at 0x00000176A9BB69E8>
    for i in range(10):      
        print(next(u), end=" ")
    print('\n')
    for i in range(12):       
        print(next(v), end=" ")
    print('\n')
    
#advanceFunGenerator();
def square(x):
    print("rahul")
    return x**2

def sum(x,y):

    return x+y;

def advanceFunMap():
    l1=[1,2,3,4,5];
    l2=[6,7,8,9,10,11,12];
    print(map(lambda x:x**2,l1))
    print(next(map(lambda x:x**2,l1)))#map reduce filter all are iterator ,next ll work
    print(list(map(lambda x:x**2,l1)))
    for i in map(lambda x:x**2,l1):
        print(i,end=' ')
    print('\n')
    for i in map(square,l1):#square fn will be called then i ll be printed
        print(i,end=' ')
    print('\n')
    for i in map(sum,l1,l2):#map fn will be called till shortest iterable is exhausted
        print(i,end=' ')    #1st,2nd ,3rd elememnt of iterables are passed in sum fun in loop
    print('\n')
#advanceFunMap()
def check(x):
    if x%4==0:
        return True
    else:
        return False;
def red(a,b):
    print("rahul in reduced function")
    #return 6# this is also fine
    return a+b
def advanceReduceandFilter():
    l1=[0,1,2,3,4,5,6,7,8,9,10]
    print(filter(lambda x: True if x%2==0 else  False,l1))
    print(list(filter(lambda x: True if x%2==0 else  False,l1)))
    print(list(filter(None,l1)))
    print(list(filter(check,l1)))
    for i in filter(check,l1):
        print(i)
    '''write check fn in such way that it returns true only in case of filtered condition
    bcz if it return true it will come in result .one element from the list will passed in each iteration'''
     
#advanceReduceandFilter()
def redu():
    l1=[0,1,2,3,4,5,6,7,8,9,10]
    print(reduce(red,l1))
    print("....................")
    l2=[];
    b=reduce(red,l2,100)
    print(b)
    '''3rd agr is optional will start adding from this. red fn should always have 2 args,2 elements from list will be passed 
    in each time .red fun will keep on executing untill iterable elements exhausted.'''
#redu();

def comp():
    l1=[12,3,4,5];
    l2=[i for i in l1];
    t1=(i for i in l1);#there is no tuple comprehension it gives generator object
    s1={i for i in l1};    
    print(l2,t1,s1,str1)
#comp();

def fileHandling():
    fp=open('chat1.txt','w+')
    fp.write('rahul kumar singh')
    fp.write('is studying Python 3\n')
    #fp.write('Python 3 supports pass by reference only')
    #fp.close();
    #fp=open('chat1.txt','r')
    for i in fp:
        print(i)
    
    print(os.getcwd())
    fp.close();
#fileHandling()

