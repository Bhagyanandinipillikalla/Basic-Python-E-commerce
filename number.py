# 1)WAPT check whether the given number is even or odd
# n=int(input())
# if n%2==0:
#     print("even")
# else:
#     print("odd")    

# 2)WAPTP sum of the numbers between m to n 
# m=int(input())
# n=int(input())
# sum=0
# while m<=n:
#     sum+=m
#     m+=1
# print(sum)    

#3)WAPTP product of the numbers between m to n 
# m=int(input())
# n=int(input())
# prod=1
# for i in range(m,n+1):
#     prod*=m
# print(prod)    

# 4)WAPT count the numbers from m to n 
# m=int(input())
# n=int(input())
# count=0
# for i in range(m,n+1):
#     count+=1
# print(count)    

# 5)WAPT swap two numbers 
# a=int(input())
# b=int(input())
# c=a
# a=b
# b=c
# print(a)
# print(b)

# 6)WAPTP square of a given number 
# n=int(input())
# print(n**2)

# 7)WAPTP cube of a given number 
# n=int(input())
# print(n**3)

# 8)WAPTP factors value of a number 
# n=int(input())
# i=1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i+=1

# 9)WAPTP factorial value of a number 
# n = int(input())
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print( fact)

# 10) WAPTP Fibonacci series 
# n=int(input())
# a=0
# b=1
# fibo=0
# while fibo<=n:
#     print(a,end=' ')
#     c=a+b
#     a=b
#     b=c  
#     fibo+=1

# 11)WAPT extract digits in reverse order 
n=int(input())
t=0
while n>0:
    num=n%10
    t=num
    n//=10
