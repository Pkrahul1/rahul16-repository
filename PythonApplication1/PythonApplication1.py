
def unpacking():
    a,b=[1,2]
    print(a,b);
    #i,j=[9,8,7,6]#error two many values to unpack
    #print(i,j)
#unpacking()
def fun():
    li=[1,2,3,4];
    li1=li;
    li1=[0,0];
    print("li1=li and li1=[0,0] only changes li1",li1,li)#li is not changed
    li1=li;
    print(li1,li)
    li1[0]=10;
    print("li[0]=10 modify both li1,li",li1,li)
    name,age=input("enter the name and age seperated by comma \n").split(",");    
    #print('my name is :{name} , age is : {age}').format();
    print(type(name),type(age));
    age=int(age);
    print(type(age))
    if type(age)==int and type(name)==str:
        print("type of age is int and name is string");
    elif type(age)!=int and type(name)==str:
        print("age should be explicitly converted to int name cant be converted to int")
    else:
        print("type of age and name is not string")
    for i in 1,2,3,4:
        print(i,end=" ")
    print('\n')
    print("....................")
    #end shd be greater than start in case of negative step no error but no o/p
    for i in range(100,10,-10):
        #continue will start the next iteration without executing the code below it.
        if i>90:
            continue;
        print(i,end=" ")
        if(i<30):
            break;
    print(" \nlist string tuple dictionary set check")
    str1="rahul"
    l1=[1,2,3,4,5,6];
    d1={"name":"rahul","zge":"23"};
    set1={0,9,8,6,3};
    tup1=(1,9,6,4,3);
    print(list(d1))#gives key indictionary
    #print("set index",set1[0]) #no indexing
    print("list comprehension");
    print([ i for i in l1])
    print(( i for i in l1),type(( i for i in l1)))#it return generator object not set of elements bcz there is no tuplw comprehension
    result=[[j for j in range(3)] for i in range(5)]#right to left
    print("1.list nested:",result)
    result=[i for j in range(5) for i in range(4)]#left to right[0,1,2,3,0,1.....]
    print("2.list nested:",result)
    result=[i for j in range(5) if j<3 for i in range(5) if i>=3]
    print("3.list nested:",result)
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
    result=[[X[i][j]+Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]#right to left
    print("2. Addition using only list comp.",result)
    listUsingComprehension=[i for i in l1]
    print("list using list comprehension:",listUsingComprehension)
    for i in d1:
        print("key:",i)
    print("keys are in list sorted on basis of value:",sorted(d1,key=lambda a:d1[a]),type(sorted(d1,key=lambda a:d1[a])))# a is each key a[0] means 1st char of string
    print("keys are in list sorted on basis of key:",sorted(d1,key=lambda a:a[0]),type(sorted(d1,key=lambda a:a[0])))
    dictionaryToSort={"abc":"rahul","zkf":"singh","jhf":"kumar","thd":"Python"}
    print("dictionary comprehension");
    dictFromComp={ i for i ,j in dictionaryToSort.items()}#will return a set
    print(type(dictFromComp),dictFromComp)
    dictFromComp={ i:j for i ,j in dictionaryToSort.items()}#will return a dictionary
    print(type(dictFromComp),dictFromComp)
#fun()
def patternFun():
    print("\n ********star print*******")
    n=int(input("enter number of lines "));
    count=1;
    for i in range(1,2*n):
        if(i<=n):
            for j in range(1,i+1):
                print("*",end="");
            k=i
            print("\n");
        else:
            for l in range(1,k-count+1):
                print("*",end="");
            count+=1;
            print("\n");
#patternFun()
def collectionList():
    list1=[];
    #list1[0]=10#error
    list1=[1,"rah",3,8,True,False,10.0];
    print(len(list1),"length of list1")
    list2=[None]*5;
    Z=[[0,1]]*4
    for i in Z:
        print(i,"id:",id(i))#all id same.
    print(list1);
    print(list2)
    list1.append(1)
    print(type(list1));
    print(list1.pop()) #remove last element and return it
    print(list1)
    print(list1.remove(1));#remove takes 1 argument to be removed and returns none 
    print(list1.remove('rah'));
    print(list1)
    l1=["rahul","kumar"]
    l2=["singh"];
    l2=l2+l1;
    print(l2);
    l1.insert(3,"rah") #if position is greater than list length it will insert at last
    print(l1[2]);
    print(l1.clear()) #returns none
    print(l1,"after clearing everything"); #clear the list
    l3=l1.copy()#return a list
    l1=[3,4]
    print(l1.count("rahul")) #return occurance of value
    l1.extend([1,2])#append as new element to list
    l1.extend({"name":"rahul","age":23})
    print("all element can be extended: ",l1)# all element can be extended:  [3, 4, 1, 2, 'name', 'age']
    print(l1[4])
    l1=[1,1,1,3,3,3,5,5,1,8,1]
    print(l1)
    print("list using range")
    for i in range(0,len(l1)):
        print(l1[i],end=" ")
    print("\n list without range\n")
    for i in l1:
        print(i,end=" ")
    print("\n")
    print(l1.index(1,2,5)) #if not found will give valueError
    print(l1.reverse()) #return none
    print(l1)
    l1.sort()#returns none
    l2=["singhh","kumarKumar","rahul"]
    l3=["singhh","kumarKumar","rahul"]
    l2.sort(key=lambda x:len(x))
    l3.sort(key=lambda x:len(x),reverse=True)
    print(l2)
    print(l3)
    l1.pop(1)#remmove at index 1 and return
    list2=[1,2,3,4,5,6,7,8,9]
    print(".........slicing...........")
    print(list2[::]) #will print whole list
    print(list2[::-1]) #will reverse list   
    print(list2[-1:-9:]) #will return empty list as start to end is backward but step is positive
    print(list2[-3:1:-1])
    print(list2[-3:1:-1]) #will return empty list as direction of step is opposite
    print("list2 in reverse order from 3rd index",list2[3::-1])#[4,3,2,1]
#collectionList()
def collectionString1():
    s1="rahulKumar"
    s2="rahul"
    print(s1,s2,sep="     ",flush=False)#sep uswed to seperate two value,flush to flush stream
    print(s1[0]);
    print(s1);
    s1="rahulsingh";
    print(s1);
    #s1[0]="s";  string is immutable ,this is called immutability
    print(s1)
    print(s1.capitalize())#return capatilized string but s1 is not changed
    print(s1)
    print("SPLIT.........................")
    s1="Rahul#kumar#singh#Python#Python3"
    l1=s1.split("#",maxsplit=2) #max 2 split will take place maxsplit is optional
    if type(l1)==list:
        print(l1)
    print("casefold.......................")
    print(s1.casefold(),"this is caseless string")#return string sutaible for caseless comparison
    print(s1.center(50,"#"))# 2nd agg is optional
    print("..........count................")
    s2="rahulrahulrahulrahul"
    print(s2.count("rah",0,17))
    print(s2.count("rah",0,18))#start end are optional,end-1 is included end is excluded 
    print(s2.endswith("rah",5,8))#start end are optional
    print(s2.find("rah",5,8))
    print(s2.index("rah",5,8))#index and find same functionality but index gives value error if 
    s3="rahul" #not found but find gives -1
    print(s3[0:4])
    if type(s2.partition("k"))==tuple:
        print("partitioned:",s2.partition("k"))
    print(s2.replace("h","j",2))#3rd arg is optional and tells how many arg to replace
    print("splitLines.........................")
    s4="rahul\nkumar\nsingh"
    print(s4.splitlines())
    print(s4.splitlines(keepends=True))
#collectionString1()
def collectionTuple():
    tup1=1,2,3,4,5,1; # or tup1=(1,2,3,4,5,1)
    tup1=2,1,3,4,5,1 
    print("tuple is :",tup1)
    print("reversed tuple:",tup1[::-1])   
    tup2=(10,)
    print("tup2 before concatanation:",tup2)
    tup2+=tup1
    print("tup2 after concatanation:",tup2)
    print("looping in tuple")
    t1=(1,)
    print(t1,type(t1))
    t2=(1)
    print(t2,type(t2))#integer
    for i in tup1:
        print(i,end=" ")
    print("\n",tup1.count(1));
    print(tup1.index(1));
    #tup1[0]=5; #cant be muted 
    print(tup1)
    a,b,c =(1,2,3)#a,b,c =(1,2,3,4) ll give error,also possible in list
    print(a,b,c,sep="  ")
    print(type(a),type(b),type(c),sep="  ")
#collectionTuple()
def collectionDict():
    dict1={
        1.0:["rahul","kumar","singh"],
        2.0:[23,24,25],    #key should be unique if duplicate key present it takes last one
        1.0:["Rah"]}                  #key can be string ,int float any immutable data type
    print(dict1)
    print(dict1.values())
    print(type(dict1.values())) 
    print(dict1.items());
    print(list(dict1.items()));
    print(type(dict1.items()))
    print(dict1.keys());
    print(type(dict1.keys()))
    d1={(1,2):"rahul"
    }
    d1[(1,3)]="singh"
    print(d1)#tuple as key
    print(d1.get((1,2)))
    print(".........print using loop.....")
    for key,value in dict1.items():
        print(key,type(key),value,type(value))
    print(".....KEYS..............")
    for key in dict1.keys():
        print(key)
    print("....looping.....")
    for key in dict1:
        print(key)
    print("........................")
    print("fromKeys",dict.fromkeys([1,2],0))
    print(dict1.get(1.0))
    print(dict1.pop('3.0',"key not found"))#if key is not there 2nd agr is returned if not given none returned
    dict1.update({3.0:"PYTHON3"})#if exist then it will override it
    print(dict1)
    print("......Sets..............")
    s1={1,2,3,4,1}
    print(s1)#duplicate removed
    #print(s1[0])#onordered doesn't support indexing
    s1={1,2}
    print(s1)
    print(type(s1))
    l1=[1,2,3,2]
    print(set(l1))
    i=10;
    print(type(i))
    s2={1,12}
    print(s1.difference_update(s2))
    print(s1)
    print(s1.symmetric_difference(s2))#return set of all element which are exactly in one of the set
collectionDict()
def stringFun1(data):
    countOfWordsDict={};
    word="";
    max=0
    frequency=0; 
    listOfWords=data.split(" ")
    for i in listOfWords:
        countOfWordsDict.update({i:listOfWords.count(i)});
    #print(type(countOfWordsDict.values()))
    listOfCounts=list(countOfWordsDict.values());
    listOfCounts.sort();
    frequency=listOfCounts[len(listOfCounts)-1];
    for key,value in countOfWordsDict.items():
        if value==frequency:
            if len(key)>len(word):
                word=key;
    print(word,frequency);
#stringFun1 ()  
def stringFun2(data):
    dataInList=data.split(" ");
    listOfEncodedWords=[];
    for i in dataInList:
        word=''
        flag=False;
        for j in i:
            if j not in ('a','i','e','o','u'):
                word+=j;
                flag=True;
        if(flag==True):
            listOfEncodedWords.append(word);
        else:
            listOfEncodedWords.append(i)
    encodedString=" ".join(listOfEncodedWords)
    return encodedString;
#stringFun2()
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    dict1={};
    m=0
    name=""
    for key,value in medical_speciality.items():
        dict1[value]=patient_medical_speciality_list.count(key);
    for key,value in dict1.items():
        if value>m :
            m=value;
            name=key
            
    speciality=name                  
    return speciality
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
#print(max_visited_speciality(patient_medical_speciality_list,medical_speciality))
def stringFun3(sentence):
    stringInList=sentence.split(" ");
    encodedList=[];
    if len(stringInList)==1:
        return sentence[::-1]
    for i in range(0,len(stringInList)-1,2):
        encodedList.append(stringInList[i][::-1])
        addstr="";
        evenStringInList=list(stringInList[i+1]);
        l1=evenStringInList.copy()
        for element in evenStringInList:
            print(element)
            if element in ('a','i','e','o','u'):
                l1.remove(element);
                addstr+=element;
         
        encodedList.append("".join(l1)+addstr);
    return " ".join(encodedList)
#print(stringFun3("WelCome"))

def funTypeCasting():
    l1=[9,10,3,1,5];
    s1={1,5,3,9,2};
    tup1=(3,6,1,9);
    str1="rahul";  
    dict1={"z1:":"rahul","a1:":"kumar","b1:":"aashu"}
    print("sorted function always return list argument can be any iterable")
    print(sorted(l1),sorted(s1),sorted(tup1),sorted(dict1),sorted(dict1,key=lambda i:dict1[i]))
    print('typecasting from one datastructure to other')
    print("converting str1 s1 tup1 dict1 in list:",list(str1),list(s1),list(tup1),list(dict1))
    print("converting str1 s1 l1 dict1 in tuple:",tuple(str1),tuple(s1),tuple(l1),tuple(dict1))
    print("converting str1 l1 tup1 dict1 in set:",set(str1),set(l1),set(tup1),set(dict1))
    #print("converting str1 s1 tup1 l1 in dict:",dict(str1),dict(s1),dict(tup1),dict(l1))
    #cant change list tuple set into dictionary;
    li=[(1,2),(3,4)]
    print(dict(li))#this is possible{1:2,3:4}
    #list(dict1),tuple(dict1),set(dict1) will convert key into list tuple and set but str(dict1)
    #will create a string containing whole dictionary "{"a":"rahul"}
    print("converting s1 l1 tup1 dict1 in string:",str(s1),str(l1),str(tup1),str(dict1))
    #when l1 is converted in string it becomes '[9, 10, 3, 1, 5]' use join to convert list into string
    print(str(l1))#it    
    print("".join([str(i) for i in l1]))
    for i in str(l1):
        print(i)
    mList=['rahul','kumar']
    mstring=str(mList)
    print(mstring)
     
    for i in range(0,5):
        print("rahul");
        i=4
        #i++ not allowed
    print(i)
    for _ in range(10):
        print(_,input())#both works fine
#funTypeCasting()

def hacker1():
    q=int(input());    
    for i in range(1,q+1):
        listofNandM=input().split();
        n=int(listofNandM[0])
        m=int(listofNandM[1]);
        sum=0;
        for j in range(1,n+1):
            p=sg(j);
            sum+=p;
        print(sum%m)
def sum(num):
    numberInString=str(num)
    sumOfdigits=0;
    for char in numberInString:
        sumOfdigits+=int(char);
    return sumOfdigits;
def sg(eachNumer):
    sumOfDigits=sum(fact(eachNumer));   
    i=1;
    while sum(fact(i))!=eachNumer:
        i+=1;         
                    
    return sum(i);

def fact(number): 
    inString=str(number);
    sum=0
    for i in inString:
        j=1;
        for k in range(1,int(i)+1):
            j*=k;
        sum+=j;
    return sum;

#hacker1()
