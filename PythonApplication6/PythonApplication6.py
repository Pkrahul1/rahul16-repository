var1=[5]
if(var1 == [5]):
    print("raul")
else:
    print("kumar")

"""

import array
import time
arr=array.array('i',[100]*1000)
t1=time.time()
arr1=arr[2:999]+arr[0:2]
t2=time.time()
print("%20.10f"%(t2-t1))
t3=time.time()
arr2=array.array('i',reversed(arr[0:2]))+array.array('i',reversed(arr[2:999]))
arr2.reverse()
t4=time.time()
print("%20.20f"%(t4-t3))
print(arr1,arr2)

from collections import Counter
def Solve (N, S):
    # Write your code here
    count=0
    n=0
    while(n<=N-2):
        str1=S[n:n+2]
        n1=n
        string1=str1
        while(n1<=N-2):
            dict1=Counter(string1)
            flag=True           
            for key,value in dict1.items():               
                if(value%2!=0):
                    flag=False
                    break          
            if(flag==True):
                count+=1
                print(string1)
            n1+=2 
            s=S[n1:n1+2]                       
            string1+=s            
        n+=1
    return count
#S="aabccbbcaa"   
S="abba"
print(Solve(4,S))

for i in range(5):
    print(i,end=" ")
    i+=3
    print(i)
print(i)
d1={(1,2):"rahul"
    }
d1[(1,3)]="singh"
print(d1)
print(d1.get((1,2)))

l2=["singhh","kumarKumar","rahul"]
l2.sort(key=lambda x:len(x),reverse=True)
print(l2)
list1=[1,2]
temp=dict(list1)
print(temp)

import itertools
from itertools import combinations
from itertools import product
print(list(itertools.chain([1,2,3],[12,12,12])))
list1=[[1,2,3],(12,12,12)]
print(list(itertools.chain.from_iterable(list1)))
print(list(combinations([1,2,3],2)))
l1=(4,5)
l2=(7,8)
print(list(product(l1,l2)))
print(list(product(l2,l1)))
print(list(itertools.chain(product(l1,l2),product(l2,l1))))

from collections import defaultdict
mapp=defaultdict(list)#if we try access value with missing key it will give default valur of list ie [].
print(mapp)
for i in range(5):
    mapp[i].append(i)
print(mapp)
for i in range(5):
    mapp[i].append(i)
print(mapp)

print("..........Matrix Multiplication...........")
from functools import reduce
import operator
def prod(iterable):
    return reduce(operator.mul,iterable,1)
X = [[1,7,3],
    [3,5,8], 
    [6,8,9]]
Y = [[1,1,1,2],
    [6,7,3,0],
    [4,5,9,1]]
resultTranspose=[list(i) for i in zip(*Y)]
result=[[sum(list(map(prod,zip(i,j)))) for j in resultTranspose] for i in X]
print("1.Multiplication using map and list comp",result)

def isFibonaci(num):
    a=0
    b=1
    c=0
    if(num==0 or num==1):
        return True
    while(num>=c):       
        if(num==c):
            return True
        c=a+b
        a=b
        b=c
for i in range(40):
    if(isFibonaci(i)):
       # print("{} is fibonaci number".format(i))
       i=2

X = [[1,7,3],
    [3,5,8],
    [6,8,9]]
Y = [[1,1,1],
    [6,7,0],
    [4,9,1]]
print("Addition using Zip")
result=[list(map(sum,zip(*i))) for i in zip(X,Y)]
print("1.Addition using map",result)
result=[[sum(j) for j in zip(*i)] for i in zip(X,Y)]
print("2. addition using nested list comp",result)
result=[[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
print("3. Addition using only list comp.",result)
Y = [[1,1,1,2],
    [6,7,3,0],
    [4,5,9,1]]
l1=[[],[],[]]
print("...Multiplication ....")
for i in range(len(X)):           
    for j in range(len(Y[0])):
        sum=0
        for k in range(len(Y)):
            sum+=X[i][k]*Y[k][j]
        l1[i].append(sum)
print("2.",l1)
print("...Transpose using Zip...")
X = [[1,7,3],
    [3,5,8],
    [6,8,9]]
Y = [[1,1,1,2],
    [6,7,3,0],
    [4,5,9,1]]
Z=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(Z)):
    for j in range(len(Z[0])):
        t=Y[j][i]
        Z[i][j]=t
print("2.Traspose of Y without ZIP:",Z)
result=[list(i) for i in zip(*Y)]
print("3.Transpose of Y using ZIP with list comp.:",result)
resultTranspose=list(map(list,zip(*Y)))
print("4.Transpose of Y using ZIP and map:",result)

result= zip(*([1,2,3],[9,8,7]))
for i in result:
    print(i)
print(result)
l1=[1,2,3,4]
l2=[10,20,30,40]
print(sum())
test_str="Geeksforgeeks"
from collections import Counter
res= Counter(test_str)
max1=max(res,key=lambda x:res[x])
print(max1)

1="rahul"
 
set1=set({})
min()
max()
sorted()
l1=[]
l1.sort()
sorted()

s1="raul"
l1=[76,98,67,45]
print(list(reversed(l1)))#reversed return iterator
sorted(l1)#sorted returns sorted list
import re
from collections import OrderedDict
d1={}
d2= OrderedDict()
d2[1]="rahul"
d2[2]="kumar"
d2[1]="singh"
for key , value in d2.items():
    print(key, value)
"""


