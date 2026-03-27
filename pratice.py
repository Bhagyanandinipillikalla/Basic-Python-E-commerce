'''(1)n=int(input())
s=1
prod=0
while s<=10:
    prod=n*s
    print(f"{n}*{s}={prod}")
    s+=1'''

'''(2)n=int(input())
c=0
s=1
while s<=n:
    if n%s==0:
        c+=1
    s+=1
if c==2:
    print("prime")
else:
    print("not a prime")'''    

'''j=int(input())
m=int(input())
n=j
sum=0
while n<=m:
    c=0
    i=1
    while i<=n:
        if n%i==0:
            c+=1
        i+=1
    if c==2:
        sum+=n
    n+=1
print(sum)'''                                    

'''n=int(input())
sum=0
count=0
temp=n
while n>0:
    count+=1
    n=n//10
n=temp    
while n>0:
    digit=n%10
    power=digit**count
    sum+=power
    n=n//10
print(sum)'''    

'''n=int(input())
sum=0
count=0
temp=n
while n>0:
    count+=1
    n=n//10
while temp>0:
    digit=temp%10
    if digit%2==0:
        power=digit**count
        sum+=power
    temp=temp//10
print(sum)'''        

'''st=input()
index=0
while index<len(st):
    ch=st[index]
    if (ch>='A' and ch<='Z') or (ch>='a' and ch<='z'):
        print(f"Alphabet:{ch}")
    elif ch>'0'and ch<'9':
        print(f"Digits:{ch}")
    else:
        print(f"special character:{ch}") 
    index+=1'''       
'''
st=input()
res=''
index=0
while index<len(st):
    ch=st[index]
    res=ch+res
    index+=1
print(res)'''

'''st=input()
index=0
dupli=st
while index<len(st):
    ch=st[index]
    if ch not in dupli:
        dupli+=ch
    elif ch in dupli:
        print(ch)
    index+=1'''

'''n=int(input())
large=n%10
while n>0:
    digit=n%10
    if(digit>large):
        large=digit
    n=n//10
print(large)  '''      

'''n=int(input())
small=n%10
while n>0:
    digit=n%10
    if(digit<small):
        small=digit
    n=n//10
print(small) '''       
      
'''st=input()
res=''
index=0
while index<len(st):
    ch=st[index]
    if ch not in res:
        res=res+ch
    else:
        print(ch)
    index+=1 '''       

'''
st=input()
word=''
index=0
while  index<len(st):
    if st[index] !=' ':
        word+=st[index]
    else:
        if word !='':
            print(word)
            word=''
    index+=1
if word !='':
    print(word)'''            

'''st=input()
index=0
res=''
while index<len(st):
    ch=st[index]
    res=ch+res
    index+=1
if res==st:
    print("pali")
else:
    print("not a pali")'''  
'''
st=input()
index=0
count=0
conso_count=0
while index <len(st):
    ch=st[index]
    if ch in 'aeiouAEIOU':
        count+=1
    elif ch not in 'aeiouAEIOU' and ((ch>='A' and ch<='z') or (ch>='a' and ch<='z')):
        conso_count+=1
    index+=1
print(count)                  
print(conso_count)'''

'''st=input()
index=0
res=''
while index<len(st):
    ch=st[index]
    if ch>='A' and ch<='Z':
        ch=chr(ord(ch)+32)
    res+=ch        
    index+=1
print(res)'''            

'''st=input()
i=0
res=''
while i<len(st):
    ch=st[i]
    if ch in 'aeiouAEIOU':
        ch='*'
    res+=ch
    i+=1
print(res)'''    

'''st=input()
i=0
while i<len(st):
    ch=st[i]
    c=0
    j=0
    while j<len(st):
        ch1=st[j]
        if ch==ch1:
            c+=1
        j+=1
    print(ch,c)
    i+=1 '''       

'''st=input()
res=''
i=0
while i<len(st):
    ch=st[i]
    if ch != ' ':
        res+=ch
    i+=1
print(res)'''        

'''st=input()
i=0
res=''
while i<len(st):
    ch=st[i]
    if ch not in res:
        res+=ch
    i+=1
print(res)'''

'''s1=input()
s2=input()
if len(s1) != len(s2):
    print("String length is not matching")
else:
    n=len(s1)
    i=0
    found=0
    while i<n:
        rotate=''
        j=1
        while j<n:
            rotate+=s1[j]
            j+=1
        rotate+=s1[0]
        s1=rotate
        if s1 == s2:
             found= 1
             break
        i+=1     
    if found == 1:
        print("rotating each other")
    else:
        print("not rotating")'''

'''st=input()
i=0
res=''
while i<len(st):
    ch=st[i]
    if ch not in res or ch == ' ':
        res=res+ch
    i+=1
if st == res:
    print("unique string")
else:
    print("not a unique")'''
'''
st=input()
found=0
i=0
while i<len(st):
    c=0
    j=0
    while j<len(st):
        if st[i] == st[j]:
            c+=1
        j+=1    
    if c==1:
            print("first:",st[i])
            found=1
            break
    i+=1
if not found:
     print("no non repeating")  '''  
'''
st1=input()
st2=input()
i=0
res=''
while i < len(st1):
    ch=st1[i]
    if ch != st2:
        res+=ch
    i+=1
print(res)'''    
'''
st=input()
i=0
res=''
while i<len(st):
    ch=st[i]
    if ch>='a' and ch<='z':
        res+=chr(ord(ch)-32)
    elif ch>='A' and ch<='Z':
        res+=chr(ord(ch)+32)
    else:
        res+=ch
    i+=1
print(res) '''           

'''
st=input()
i=0
while i<len(st):
    j=i
    while j<len(st):
        substring=st[i:j+1]
        print(substring)
        j+=1
    i+=1 '''   

'''s1=input()
s2=input()
if len(s1) != len(s2):
    print("Not isomorphic")
else:'''

'''st=input()
i=0
seen=[0]*26
while i<len(st):
    ch=st[i]
    if (ch >= 'A' and ch <='Z'):
         ch=chr(ord(ch)+32)
    if ch >= 'a' and ch <= 'z':
        index =ord(ch)-97
        seen[index]=1
    i+=1
j=0
c=0
while j<26:
    c+=seen[j]
    j+=1
if c == 26:
    print("pangram")
else:
    print("Not a pangram") ''' 

'''st=input()
i=0
res=''
while i<len(st):
    ele=st[i]
    if ele not in res:
        res+=ele
    i+=1
print(res)'''              

'''l=[32,9,3,43,25]
i=0
res=[]
while i<len(l):
    ele=l[i]
    if ele<10:
        print(ele)
    else:
        st=str(ele)
        j=0
        res=''
        while j<len(st):
            ch=st[j]
            res=ch+res
            j+=1
        print(res)
    i+=1 '''              
'''
n=int(input())
m=int(input())
sum1=[]
l1=[]
l2=[]
i=0
while i<n:
    ele1=int(input())
    i=i+1
    l1=l1+[ele1]
j=0
while j<m:
    ele2=int(input())
    j+=1
    l2=l2+[ele2]

k=0
while k<len(l1):
    sum1=sum1+[l1[k]+l2[k]]
    k=k+1
print(sum)'''
        
'''n=int(input())
last=n%10
first=n
while first>=10:
        first=first//10
sum=first+last
print(sum)'''  
                


# n=1
# m=100
# while n<=m:
#     num=n
#     c=0
#     i=1
#     while i<=n:
#         if n%i==0:
#             c+=1
#         i+=1
#     if c==2:
#         print(num) 
#     n+=1           
        


     
                
