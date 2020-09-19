
import numpy as np

l1=[1,2,3,4]
l2=[2,3,4,5.0]
l3=["ab','bc","ca","da"]
l4=[5,4,3,2]
#arr=np.array(l1,l3)#array contains data of one type

arr=np.array(l1)
print(arr)
print(type(arr))
print("......................")     
arr1=np.array([l1,l2,l3])#all element converted to float
arr2=np.array([l1,l2])
print(arr2)
print(arr1)
print(type(arr),"type of each row")

print(arr1[0])
print(type(arr1[0][0]),'type of each element')
print(arr1.shape)
arr=np.array(l2)
arr1=arr.reshape()
#pandas begins here






