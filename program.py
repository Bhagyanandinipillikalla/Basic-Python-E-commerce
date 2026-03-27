# n=int(input())
# m=int(input())
# try:
#     r=n//m
#     print(r)
# except ZeroDivisionError:
#     print("zero not in denom")    
# print("hello")

# a=10
# try:
#     st=eval(input())
#     print(st)
# except NameError:
#     print("value not there")    

# st=input()
# try:
#     n=int(input())
#     print(st[n])
# except Exception as e:
#     print(e)

# s=input()
# try:
#     n1=int(input())
#     print(s[n1])
#     print("hello")
# except Exception as e:
#     print(e)


# finally:
#     a=int(input())
#     b=int(input())
#     print(a+b)

# n=int(input())
# try:
#     m=int(input())
#     st=input()
#     print(n+st)
#     print(n+m)
# except TypeError:
#     print("enter")
# except ValueError:
#     print("invalid")
       

# age=int(input())
# if age<18:
#     raise Exception("not eligiblr")
# else:
#     print("elibliytr")

# class Rani(Exception):
#     def __init__(self,message):
#         self.message=message
#     def __str__(self):
#         return f"customer error:{self.message}"
#     def __repr__(self):
#         return f"Rani('{self.message}')"
# for i in range(4):
#     raise Rani("send")         

# while True:
#     print("hii")       



# l=[2,4,6,8][::-1]
# m=[]
# for i in range(len(l)):
#     n=l[i]
#     m+=[n*i]
# print(m)

# a=eval(input())
# b=a.reverse()
# out=[]
# for i in range(len(a)):
#     c=a[i]
#     out+=[c*i]
# print(out)    

# l=[2,3,4,5]


# l=[32,90,56]
# res=[]
# for i in range(len(l)):
#     ele=l[i]
#     sum=0
#     while ele>0:
#         digit=ele%10
#         sum+=digit
#         ele//=103.
#     res+=[sum]
# print(res)


# out={}
# for i in range(65,91):
#     out[chr(i)]=i
# print(out)    


# a={'a':'a','b':'c','c':'c','d':'e',(1,2):(1,2)}
# for i in a:
#     if i==a[i]:
#         print(i,a[i])

# a='power star'
# out={}
# b=a.split()
# for i in b:
#     c=0
#     for j in i:
#         c+=1
#     out[i]= c   
# print(out)

# a='power star'
# b=a.split()
# out={}
# for i in b:
#     count=0
#     for j in i:
#         if j in 'aeiouAEIOU':
#             count+=1
#     out[i]=[len(i),i[::-1],count]
# print(out)    