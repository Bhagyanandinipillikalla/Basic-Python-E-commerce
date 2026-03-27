'''s=input()
if 'A'<s<'Z':
    print('uppercase')
elif 'a'<s<'z':
    print('lowercase')
elif '0'<s<'9':
    print(f'{s}digit')
else:
    print(f'{s} is special character')'''            

'''i=input()
if 'a'<i<'z':
    print(chr(ord(i)-32))
elif 'A'<i<'Z':
    print(chr(ord(i)+32))   
elif '0'<i<'9':
    print(int(i)**2)     
else:
    print(ord(i))''' 

#instagram login page
'''username=input()
password=input()
if username=='bhagya' and password=='bha@12':
    print('suss')
else:
    print('fail') '''   



#j=int(input('j:'))
#for j in range (j%2!=0):
    #print(f'{j}oddnumber')


#i=int(input())
#while i%2!=0:
#    print(i)


#sum of first 10 numbers
'''value=0
i=1
while i <= 10:
    value+=i
    i+=1
print(value)'''    

#print factorial n numbers

'''fact = 1
for i in range(1,6):
a=int(input("a="))
b=int(input("b="))
print(f"before swap:\na={a}\tb={b}")
    fact*=i
    print(fact)'''
    
    
'''l=[3,26,37,87]
m=[4,98,6,45]
sum=[]
i=0
while i<len(l):
    sum=sum+[l[i]/m[i]]
    i+=1
print(sum)'''  

st=input()
for i in range (0,len(st)):
    ch=st[i]
    if i%2!=0:
        print(ch)

st="Morning" 
i=0
while i<len(st):
    ele=st[i]
    if i%2!=0:
        print(ele)
    i+=1   
        