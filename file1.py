'''print("hello")
a=int(input('enter the vlue: '))
print(a)
b=float(input())
print(b)
c=a+b
print(c)
a=int(10.0)   #it convert float to int
print(a)    
b=float(20)    #it convert int to float
print(b)
c=a+b
print(c)'''




'''a=int("100")
print(a)
b=int("6.8")
print(b)
c=int("1+2j")
print(c)
d=int("shan")
print(d)
e=int(100)
print(e)
f=int(8.9)
print(f)
g=int(9+8j)
print(g)'''


'''row=int(input('row:'))    
col=int(input('col:'))               
for i in range (row):
    val=col
    for j in range(col):
        print(val,end=' ')
        val-=1
    print()'''

     
'''row=int(input('row:'))
col=int(input('col:'))
for i in range(row):
    row+=1
    for j in range(col):
        print('*',end='')
        row+=1
    print() '''   


row=int(input('row:'))
col=int(input('col:'))
for i in range(row):
    for j in range(col):
        print('*',end=' ')
        row+=1
    print()        