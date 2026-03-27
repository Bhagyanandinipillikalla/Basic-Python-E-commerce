'''def nandini():
    print('i am nandini')
def bhagya():
    print('hallo i am bhagya')
def reddy():
    print('this is reddy')
nandini()    
bhagya()
reddy()    
nandini()    
bhagya()
reddy() '''


'''def sumofnum(a,b):
    print(a+b)
sumofnum(2,5)  
sumofnum(2,9)'''  


'''def product(a,b,c):
    print(a*b*c)
 product(1,2,3)'''

'''def evenorodd(n):
    if n%2 == 0:
        print('even')
    else:
        print('odd')
evenorodd(7)            
evenorodd(4)'''

'''
def checkdivisor(i):
    if 25%i==0:
        print('yes')
    else:
        print('no')
checkdivisor(50)
checkdivisor(5)
checkdivisor(100)'''

'''def seriesofnum(a,b):
    while a<=b:
        print(a)
        a+=1
seriesofnum(1,5)'''


'''def checkevenorodd(n):
    i=1
    sum=0
    while i<=n:
        sum+=i
        i+=1
    if sum%2==0:
        print('even')
    else:
         print('odd')
checkevenorodd(5)    
checkevenorodd(3)'''

'''
def series():
    start=1
    n=10
    while start<=n:
        print(start)
        start+=1
series() '''

'''def checksum():
    a=1
    b=5
    sum=0
    while a<=b:
        sum+=1
        a+=1
    if sum%2==0:
        print('even')
    else:
        print('odd')
checksum()'''             


'''
n=int(input())
while n>0:
    digit =n%10
    sum=0
    start=1
    while start<=digit:
        sum+= start
        start+=1
    print(sum)
    n=n//10''' 

'''def sumofdigit(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    print(sum)
sumofdigit(123)'''        

'''def intputnum(n):
    count=0
    while n>0:
        count+=1
        n=n//10
    print(count)
intputnum(256)'''     

'''def factnum(n):
    i=1
    fact=1
    while i<=n:
        fact*=i
        i+=1
    print(fact)
factnum(3)'''       

'''n=int(input())
finalsum=0
while n>0:
    digit=n%10
    sum=0
    start=1
    while start<=digit:
        sum+=start
        start+=1
    finalsum+=sum
    n=n//10
print(finalsum)''' 

'''n=int(input())
finalprod=0
while n>0:
    digit=n%10
    prod=1
    start=1
    while start<=digit:
        prod*=start
        start+=1
    finalprod+=prod
    n=n//10
print(finalprod)'''

'''n=int(input())
n1=n 
n2=n
count=0
sum=0
while n>0:
    count+=1
    n//=10
while n1>0:
    digit=n1%10
    power=digit**count
    sum=sum+power
    n1//=10
if(sum==n2):
    print('yes')
else:
    print('no')''' 

'''n=int(input())
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
reverse=0
while sum>0:
    digit=sum%10    
    reverse=reverse*10+digit
    sum=sum//10  
print(reverse)'''

'''n=int(input())
prod=1
while n>0:
    digit=n%10
    prod*=digit
    n=n//10
sum=0
prod1=1
while prod>0:
    digit=prod%10
    sum+=digit
    prod1*=digit
    prod//=10
if prod1==sum:
    print('spy') 
else:
    print('not a spy')'''       

'''n=int(input())
fact=1
i=1
while i<=n:
    fact*=i
    i=i+1
r=0    
while fact>0:
    digit=fact%10
    r=r*10+digit
    fact//=10    
if(r==fact):
    print('palindrom')
else:
    print('not a palindrom')'''         



'''def f1():
    a=10
    print(a)
def f2():
    a=20
    print(a)
f1()
f2()'''


'''a=50
def f1(num):
    global a
    a=10
    print(a)
    print(num)
def f2(num):
    a=20
    print(a)
    print(num)
f1(98)
f2(56)        
print(a)'''
    
'''ch=input()
if(ch>='0' and ch<='9'):
    print(ord(ch))
else:
    print('no')'''

'''ch=input()
if not((ch>='A' and ch<='Z')or(ch>='a' and ch<='z')or(ch>='0'and ch<='9')):
    print('alpha')
else:
    print(ch*3)'''            

'''ch=input()
if ch>='A' and ch<='z' and ord(ch)%2!=0:
    print(chr(ord(ch)+1))
else:
    print(chr(ord(ch)-1))'''    


'''def info(name,age):
    print(f"the name is {name}")
    print(f"the age is {age}")
info('bhagya',22) 
info(22,'bhagya')
info(name='bhagya',age=22)  
info('nandini',age=22)
#info(name='bhagya',22) syntaxError'''


'''def info(name,age=18,address='tirupati'):
    print(f"the name is {name}")
    print(f"the age is {age}")
    print(f"the address is {address}")
info('Bhagya')
info('Nandini',22,'Banglore')
info('nandini',21)
info('bhagya',21,'Banglore')
info(address='kadapa',name='reddy',age=21)'''    


'''def sum(*a):
    print(a)
    sum=0
    for i in a:
        sum+=i
    print(sum) 
sum()
sum(0)
sum(1)
sum(1,2,3)
sum(1,2,3,4,5)'''       
    
'''def sum(**info):
    print(info)
sum(name='bhagya',age=22)
sum('nandini',22)'''    

'''def greet(name,age):
    print(f"Hello {name},you are {age} ears old")
person1=["alexa",22]
person={'name':'bob','age':25}
greet(*person1)
greet(**person)'''

'''st=input()
count=0
index=0
while index<len(st):
    ch=st[index]
    if((ch>='0' and ch<='9') and index%2==0):
        count+=1
    index+=1
print(count)'''        

'''st=input()
count=0
index=0
while index<len(st):
    ch=st[index]
    if((ch>='A' and ch<='Z') or (ch>='a' and ch<='z')) and index%2!=0:
        count+=1
    index+=1
print(count)'''

'''st=input()
count=0
index=0
while index<len(st):
    ch=st[index]
    if((ch>='A' and ch<='Z') or (ch>='a' and ch<='z')) and ord(ch)%2==0:
        count+=1
    index+=1
print(count)'''     

'''st=input()
count=0
index=0
while index<len(st):
    ch=st[index]
    if (ch not in 'aeiouAEIOU') and (ch>='a' and ch<='z'):
        count+=1
    index+=1
print(count)'''        
    
   
'''st=input()
count=0
index=0
while index<len(st):
    ch=st[index]
    if ch=='A' or ch=='a':
        count+=1
    index+=1
print(count)'''        
   
'''st=input()
index=0
res=""
while index<len(st):
    ch=st[index]
    if (ch in 'aeiouAEIOU') or ch==" ":
        res=res+ch
    index+=1
print(res)          

st=input()
index=0
res=""
res1=''
while index<len(st):
    ch=st[index]
    if (ch not in 'aeiouAEIOU'):
        res=res+ch
    if ch in 'aeiouAEIOU':
        res1+=ch
    index+=1
print(res)
print(res1)


Q4st=input()
index=0
res=""
space=1
while index<len(st):
    
    ch=st[index] 
    if ch==' ':
       space+=1
    if space%2==0:
      if (ch not in 'aeiouAEIOU') or (ch not in '0123456789'):
        res=res+ch
    index+=1
    
print(res)  

st=input()
index=0
res=""
res1=''
res2=""
res3=''
while index<len(st):
    ch=st[index]
    if   (ch not in 'aeiouAEIOU') and ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
        res+=ch
    if ch in 'aeiouAEIOU':
        res1+=ch
    if ch>='0' and ch<='9':
        res2+=ch  
    if not ((ch>='a' and ch<='z') or (ch>='A' and ch<='Z') or (ch>='0' and ch<='9')):
        res3=ch+res3      
    index+=1
print(res,end=',')
print(res3,end=',')
print(res1,end=',')
print(res2)
'''


'''st=input()
res=''
index=0
while index<len(st):
    ch=st[index]
    if ch>='A' and ch<='Z':
        res+=chr(ord(ch)+32)
    else:
        res=res+ch
    index+=1

i=0

res1=''
while i<len(res):
    ch1=res[i]
    if ch1 in 'aiou':
        res1=res1+"*"
    elif ch1=='e':
         res1=res1+'$'
    else:
         res1+=ch1
    i+=1
print(res1)'''

            
'''class Phones:
    com=None
    ram=None
    cost=None
    color=None
    dis=None
    battery=None
    cam=None
    network=None
    def initialize(self,d1,d2,d3,d4,d5,d6,d7,d8):
        self.com=d1
        self.ram=d2
        self.cost=d3
        self.color=d4
        self.dis=d5
        self.battery=d6
        self.cam=d7
        self.network=d8
    def display(self):
        print(self.com,self.ram,self.cost,self.color,self.dis,self.battery,self.cam,self.network)
p1=Phones()
Phones.initialize(p1,"vivo",'8gb',20000,'biue',16*16,'12hours','12px','5g')
p1.display()'''      
            

'''class student:
    name=None
    age=None
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
s1=student("meena",23)
s2=student(name="meera",age=21)
s1.display()
s2.display()'''

class person:
    name=None
    age=None
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):

        print(f"My name is{self.name}")
class student(person):
    standard=None
    gender=None
    def __init__(self,standard,gender,name,age):
        self.standard=standard
        self.gender=gender
        person. __init__(self,name,age)
    def study(self):
        print(f"{self.name} is studing {self.standard} stand")    
class sport:
    sname=None
    def __init__(self,sname):
        self.sname=sname
    def game(self):
        print(f"plays {self.sname}")  
class collegestudent(student,sport):
    clgname=None
    def __init__(self,clgname,sname,standard,gender,name,age):
        self.clgname=clgname
        student.__init__(self,standard,gender,name,age)
        sport.__init__(self,sname)
    def display(self):
        student.study(self)
        sport.game(self)
        print(self.clgname)
c1=collegestudent("geetham","shuttle",11,"female","rani",18)
c1.display()
c1.game()
c1.study()
    


































