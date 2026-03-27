'''d={}
d['name']='Rani'
d['age']=21
d['gender']='Female'
print(d)'''


'''d={'name':'Vani','age':21}
key='age'
if key in d:
    print("key exists")
else:
    print("key not exists")'''

'''d={}
n=int(input())
i=1
while i<=n:
    d[i]=i*i
    i+=1
print(d)'''

'''n=int(input())
d={}
for x in range(1,n+1):
    d[x]=x*x
print(d)'''   

'''n="this is a test is easy test" 
d={}
i=0
while i<len(n):
    ele=n[i]
    if ele in d:
        d[ele]=d[ele]+1
    else:
        d[ele]=1
print(d)'''

'''d={'a':1,'b':4,'c':5}
sum=0
for key in d:
    sum=sum+d[key]
print(sum)'''    


'''d={'a':1,'b':4,'c':5}
prod=1
for key in d:
    prod=prod*d[key]
print(prod)'''   


'''d={'a':1,'b':4,'c':5}
key='c'
if key in d:
    del d[key] 
print(d)'''     