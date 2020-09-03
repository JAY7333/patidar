print('Jay Patel')

x=5
if x<10:
    print('Smaller')
if x>20:
    print('bigger')
print('finis')

x=5
while x>0:
    print(x)
    x=x-1
print('blastoff')

x=5
n=10
while n>0:
    x=x+x
    print(x)
    n=n-1
print("Bazuka")

x=1+2
print(x)
abc='bcd'+'cde'
print(abc)
x=float(x)
type(x)

int('123')
#int('xyz')

name=input('who are you?')
print("welcome",name)
name=input('who are you?')
print("welcome"+name)

#comments

#Convernt elevator flooors
inp=input("European Floor?")
usf=int(inp)+1
print("US Floor =",usf)

for i in range(5):
    print(i)
    if i>2:
        print("Bigger than 2")
    print("Done with",i)
print("all done")

#if else
x=input("what is x?")
x=int(x)
if x<0 and x%2==0:
    print(x,"is negative as well as even")
elif x>0 and x%2!=0:
    print(x,"is posite and odd")
else:
    print(x,"you are useless")
print("done")

#try except
x=input("please type number")
try:
    x=int(x)
except:
    x= "x"
if x=="x":
    print("where is your common sence")
else:
    print("brillient")


hour=input("how many hour did you work for this week: ")
rate=input("rate per hour")
try:
    hour=float(hour)
    if hour<40 :
        print("your wage= ", (hour*(float(rate))))
    else:
        print("your wage= ", (hour*(float(rate))*1.5))
except:
    print("YOU SHOUD INPUT HOUR IN NUMBER")


#function 
def thing():
    print("Hello")
    print("Wellcom")
thing()
print("Mr Khan")
thing()


max("Hello world")
min("Hello World")

#Define function
def nam(Jay):
    if Jay==123:
        print("Patel")
    elif Jay=="a":
        print("Arvindkuar")
    else:
        print("Jay")
nam(123)
nam('a')
nam(124)

#return
def jay():
    return 1
print(jay())

def greet(lan):
    if lan=="en":
        print("Hello")
    elif lan=="hi":
        return "Namaste"
    else:
        return "NA"        
print(greet("en"),"Jay")
print("patel",greet("hi"))
print(greet("svsfgs"),"Arvindkumar")

def plus(a,b):
    x=a+b
    return x
print(plus(12,25))
print (plus(12,-12))

def computepay(h,r):
    if h>40:
        df=((40*r)+((h-40)*r*1.5))
        return df
    else:
        df=h*r
        return df
h=input("numver of hour")
r=input("rate per hour")
p = computepay(float(h),float(r))
print("Pay",p)

#Breaking the loop
while True:
    line=input(">")
    if line=="done":
        break
    print(line)
print("Done")

#finishing the iteration with continue
while True:
    x=input(">")
    if x[0]=="#":
        continue
    elif x=="done":
        break
    print(x)
print("DONE")

for i in [1,2,3,4,5,6]:
    print(1/i)
rama=["a","B","c","D","e","F","g","H"]
for i in ["patel","jay","arvindkumar"]:
    print(i+"ramash")
for i in rama:
    print(i)


# largest number in list
largest_so_far=-1
print("before",largest_so_far)
list1=[1,25,63,89,14,25,36,78,52,36,55,63,69,41,25,36,48,69,94,53,21,56,25,4,62,5,6,5,52]
for num in list1:
    if num>largest_so_far:
        largest_so_far=num
    print(largest_so_far,num)
print("after",largest_so_far)

#counting in the loop
zoop=0
print("before",zoop)
x=[1,1,6,56,5,5,5,5,5,5,5,5,5,6,6,6,6,6,3,3,223,2,1,2,25,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6]
for n in x:
    zoop=zoop+1
    print(zoop,n)
print("after",zoop)

saga=0
print("before",saga)
for n in x:
    saga=saga+n
    print(saga,n)
print("after",saga)

#average of the loop
saga=0
ave=0
print("before",saga,ave)
for n in x:
    saga=saga+1
    ave=(ave+n)
    mean=ave/saga
    print(saga,ave,mean)
print("after",saga,ave,mean)

#Filtering in the loop
for n in x:
    if n>20:
        print(n,"is grater than 20")
print("byebye")

#found variable using boolinan variable
found=False
print("before",found)
for n in x:
    if n==3:
        found=True
    print(found,n)
print("after",found)

#found smallest variable using None
small_so_far=None
for n in x:
    if small_so_far is None:
        small_so_far=n
    elif n<small_so_far:
        small_so_far=n
    print(small_so_far,n)
print("smallest value is",small_so_far)
    
#Exerciese
flo=0.0
num=0
while True:
    n=input("enter number ")
    if n=="done":
        break
    else:
        n=float(n)
        flo=flo+n
        num=num+1
        print(num,flo)
print("Done")


flo=0.0
num=0
while True:
    n=input("enter number ")
    if n=="done":
        break
    else:
        try:
            n=float(n)
            flo=flo+n
            num=num+1
        except:
            print("invalid input")
            continue
            
print("Done",flo,num,flo/num)
    

#exercise import
largest=None
smallerst=None
while True:
    x=input("Enter a number")
    if x=="Done":
        break
    else:
        try:
            x=float(x)
            if largest is None:
                largest=x
                smallerst=x
            else:
                if x>=largest:
                    largest=x
                elif x<=smallerst:
                    smallerst=x
        except:
            print("Invalid input")
            continue
print("Maximum is",largest)
print("Minimum is",smallerst)
