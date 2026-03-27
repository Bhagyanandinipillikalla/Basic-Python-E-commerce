# print(len('[10,20,30]'))

# def sum(*a,b):
#     return a+b
# print(sum({1:20},20))    

# n=int(input())
# if n&1==0:
#     print("even")
# else:
#     print("odd")    

# matx1=[[1,2,3],[4,5,6]]
# matx2=[[1,2,3],[2,9,3]]
# sum=[]
# for i in range(len(matx1)):
#     res=[]
#     for j in range(len(matx2[0])):
#         res+=[matx1[i][j]+matx2[i][j]]
#     sum+=[res]    
# print(sum)    

# def rotate_90(matrix):
#     n=len(matrix)
#     for i in range(n):
#         for j in range(i,n):
#             matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
#     for row in matrix:
#         row.reverse()
#     return matrix
# mat=rotate_90([[1,2,3],[4,5,6],[7,8,9]])
# print(mat)    

# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# num=int(input())
# if prime(num):
#     print("prime num")
# else:
#     print('not a prime')   

# def sorted(st):
#     l=list(st)  
#     print(len(l),l)
#     for i in range(len(l)):
#         for j in range(len(l)-i-1):
#             if l[i]>l[j+1]:
#                 temp=l[i]
#                 l[i]=l[j+1]
#                 l[j+1]=temp
#     return "".join(l)
# st1=input()
# st2=input()
# if len(st1)==len(st2) and sorted(st1)==sorted(st2):
#     print('Anagram')
# else:
#     print("not a anagram")                   
   
# n=int(input())
# for i in range(2,n+1):
#     c=0
#     for j in range(1,i+1):
#         if i%j==0:
#             c+=1
#     if c==2:
#         print(i)    

# n=int(input())
# for i in range(1,n+1):
#     print('*'*i)

# s="kabab is love"
# words=s.split()
# print(words)
# out={}
# for word in words:
#     rev=word[::-1]
#     count=len(word)//2
#     half=word[:2]
#     out[word]=[rev,count,half]
# print(out)    


# def outer(a,b):
#     def inner():
#         print(a+b)
#     return inner
# s=outer(6,8)
# s()    

# def fun():
#     print("Hello")
# def add(f1):
#     f1()
#     print("Adding")
#     print("Bye")
# add(fun)        


# l1=['hello','bye','good']
# print(list(map(lambda st:st[::-1].upper(),l1)))

# l=[1,2,3,4,5,6,2]
# print(list(filter(lambda n:n%2==0,l)))

# l=[1, 2, 3, 4, 5]
# print(list(map(lambda n:n*n,l)))

# m=["hi", "hello", "python"]
# print(list(map(lambda a:a.upper(),m)))

# n=[2, 4, 6, 8]
# print(list(map(lambda a:a+10,n)))

# p=[11, 12, 13, 14, 15, 16]
# print(list(filter(lambda n:n%2==0,p)))

# div=lambda n:n%5==0
# print(div(25))


# a=[10, 20, 30]
# print(list(map(lambda n:str(n),a)))

# l=["Anu", "Bhagya", "Asha", "Kiran"]
# print(list(filter(lambda a:a[0]=='A',l)))

# m=[1, 2, 3, 4, 5, 6]
# print(list(map(lambda a:a*2 if a%2==0 else a,m)))

# p=["cat", "tiger", "lion", "elephant"]
# print(list(filter(lambda a:len(a)>4,p)))

# b=["apple", "banana", "kiwi"]
# print(list(map(lambda a:len(a),b)))


# a = [10, 20, 30]
# b = [1, 2, 3]
# print(list(map(lambda a,b:a+b,a,b)))

# m=[3, 6, 9, 12, 15, 18]
# print(list(filter(lambda a: a%2==0 and a%3==0,m)))

# n=[-5, 10, -2, 3, -8]
# print(list(map(lambda a: a<0,a)))

# p=[(1, 5), (3, 1), (2, 4)]
# a=sorted(p,key=lambda a:a[1])
# print(a)

# q=[2, 3, 4, 5]
# print(list(map(lambda a:a**3,q)))



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def addfirst(self,data):
        newNode=Node(data)
        if self.head==None and self.tail==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.head.prev=newNode
            newNode.next=self.head  
            self.head.next=newNode
            newNode.prev=self.head 
            self.head=newNode     
    def display(self):
        n=self.head
        print(n.data,end=" ")
        while n.next!=self.head:
            print("--->",n.data,end=" ")
            n=n.next
d=DLL()
d.addfirst(88)
d.addfirst(25)
d.display()     