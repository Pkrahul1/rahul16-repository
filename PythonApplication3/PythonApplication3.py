def returntwo():
    return 1,2
#print(returntwo(),type(returntwo()))
print("...function can be assigned to variable, can passed as argument, can refurn a function....")
print(".....this is called first class function....")
def multiply(mul):
    def innerfunction(innermul):
        return mul*innermul
    print(innerfunction(30)) #calling function inside function.
    return innerfunction #returning function not calling
#var1=multiply # not calling multiply function just assigning function to variable.
#print(var1(10))
#print(var1(10)(100))
#var2=multiply(10) # var2 wll store innerfunction returned , but here we are calling multily function
#print(var2(20))
def printname(func):
    print(func("rahul kumar"))
def passname(name):
    return name
#printname(passname)#passname fn is passed as argument 
print(".....decorators in pyhton......")
def dec_msg(fun):
    print("inside decorator at top")
    i=fun
    print(i,fun)
    def addWelcome(name):
        print(name)
        print("inside of inside function")
        print("Welcome " + fun(name) +fun1())#calling printname function, from inside we can call outer function as well(fun1)
        return "Welcome " + name
        
    print("inside dec_msg at bottom")
    return addWelcome
@dec_msg
def printname(name):
    print("inside printname")
    return name
def fun1():
    return " habing fun ??"
b=printname("rahul")#b=printname() will give error 
#writting above statement means we are directly calling addWelcome funstion with parameter, name will have rahul,same signtr
#it will automaticly call decorator function and executes its body, fun will have printname.
print(b)
print('decorator with params........')

print('............immutable.....................')
def fun(num): 
    print(id(num),'id of num before chanaging value')#id is same as i(num and i is reference of same obj till now
    num=10;
    print(id(num),'id of num after changing value')#id is different from i as int is immutable and creates new object
                  #when assigned a new value 
#i=1;
#print(i);
#print(id(i),'id of i outside before fn call')
#fun(i);
#print(id(i),'is of i outside after fn call')
#print(i)
print('............mutable.....................') 
def fun1(list1):
    list1[0]=1;
    print(id(list1),'id inside')#list1=l1 , so list1 is referring same object as l1 any changes 
#l1=[10,11]      #in list1 will be reflected outside also as list is mutable
#print(l1);
#print(id(l1),'id outside')
#fun1(l1);
#print(l1)
'''python only support pass by reference but if object is mutable changed made inside
function will be reflected outside .if immutable changes are reflected localy inside '''
print('...........global variable................')
global_variable=1;
def globalCheck():
    global_variable=10;
#globalCheck()
#print(global_variable)
'''global variablecant be accessed inside function, it created a new local variable
with same name .To use global variable defind variable using global keyword.'''
def globalCheck1():
    #globaldict_values=0;
    #print(global_variable);#uncommenting these two line will give arror
    global global_variable;
    global_variable=100;#we are using global variable
    print(global_variable);
#globalCheck1();
#print(global_variable);
def fun(*argv):
    print(*argv,type(argv))
    print(argv,type(argv))
l1=[1,2,3]
#fun(*l1)# * is used to unpack,*l1 means we are passing 1,2,3. l1 means we are passing list l1 as one variable
def argKwarg(*argv,**kwarg):#arg for non-keywaord argum ents and **kwarg for  keywords arguments 
    print(argv)
    print(kwarg)  #kwarg is dictionary here
def kwarg(a,b): # def kwarg(**dict1) # tis wll also work,dict ll be dictionary in this case
    print(a,b,sep="  ") # a, b sud be same as key of dictionary, 
dict1={"a":"rahul","b":"kumar"}
#kwarg(**dict1)
#argKwarg(1,2,3,first="rahul",last="kumar")
def funCheck(num1,*num2,n1,num3=1,num4=2,n2,**dict1):#funCheck(nun1,*num2,num3=1) this will also work
    #num2 will be a tuple dict1 will be dictionary
    print("success")       
    for i in num2:
        print(i,end=' ')
    print('\n',num3,num4,n1,n2)
    print(dict1,type(dict1))
#funCheck(1,2,3,4,5,n1=10,n2=5,a=100,b=200)
'''defaults arg and variable arg both should be in last in any order keyword agrs 
can be anywhere after positional args'''

print('.....exceptionHandling..........')
def exceptionHandling(i):
    try:
        j=i/0;
    except ZeroDivisionError:
        print("zero division error")
    except NameError:
        print('Name error')
    except:
        print('some other error. default except should be in last')
    finally:
        print('in finally no matter error occured or not')
        print('control will go after exception')
    print("outside try-except-finally")
#exceptionHandling(10)
#print('ouside function');
def exceptionHandling1():
    try:
        j=i/0;
    except ZeroDivisionError:
        print("zero division error")
    except NameError:
        print('Name error')
    except:
        print('some other error. default except should be in last')
    finally: 
        print('in finally no matter error occured or not')
        print('control will go after exception')
    print("outside try-except-finally")
     
#try:
    
#    #exceptionHandling1();
#    #print('outside exception');
#except NameError: 
#    print('name error wont be executed as its already met in fun try except block')
#print('outside everything')
'''last except is default .after except control will go from where it was called.'''
"""custome exception can be used by inhereting exception class"""
class CustomeException1:
    def exception1(self):
        l1=[1,2,3]
        i=4
        try:
            #raise Exception("raising default exception")#this will raise default exception.
            if i not in l1:
                raise InvalidElement #InvalidElement("exception from exceptin1 method") use line 139
        except InvalidElement as e:
            print("elements not in list")
            #print(str(e))
        except Exception as e:
            print(str(e))
class InvalidElement(Exception):
    pass
ce=CustomeException1()
ce.exception1()





