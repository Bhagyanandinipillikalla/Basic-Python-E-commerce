#To check entered character is special character or not
#char=input('enter:')
#if not('a'<char<'z' or 'A'<char<'Z' or '0'<char<'9'):
#    print('Special character')
#else:
#    print('Not special character')    

#To check upper to lower and lower to upper and digit to squre of digit and special character to ASCII value
#i=input('enter:')
#if 'a'<=i<='z':
#    print (chr(ord(i)-32))
#elif'A'<=i<='Z':
#    print(chr(ord(i)+32))
#elif'0'<=i<='9':
#    print(int(i)**2)
#else:
#    print(ord(i))                

#Create instagram login page
#username=input('username:')
#password=input('password:')
#if username=='Bhagya':
#    if password=='Bha@123':
#       print('login success')
#    else:
#       print('wrong password') 
#else:
#    print('wrong username')          

#To print sum od first 5 numbers
#n=int(input('n:'))
#sum=0
#for i in range(1,n+1):   
#    sum+=i
#print(sum) 

#To print factorial of n natural number
#n=int(input('n:'))
#f=1
#for i in range(1,n+1):
#   f*=i
#print(f)
'''n=int(input())
start=1
prod=1
while n>0:
    digit=n%start
    prod=digit*1
    start+=1
print(prod)'''

'''def outer():
    print("outer")
    def inner():
        print("inner")
    print("Excecuted")
    inner() 
outer()'''    
        
'''def outer():
    print("outer")
    def inner():
        print("wow")
    return inner
v=outer()
v()'''  
'''def outer(a,b):
    def inner():
        print(a,b)
    return inner
s=outer(21,3)
s() '''        
'''def f1():
    print("zing zang")
def outer(fu):
    def inner():
        fu()
    return inner
f=outer(f1)
f()'''  

