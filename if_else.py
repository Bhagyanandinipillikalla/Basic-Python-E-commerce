#1. WAP to check whether a number is positive or negative. If Positive print positive message or else print Negative Number.
# num=int(input())
# if num>0:
#     print(f"{num} is positive number")
# else:
#     print(f"{num} is negative number")    

#2.WAP to check whether a number is even or odd. If even, print message an even or else print message as odd.
# num=int(input())
# if num%2==0:
#     print("Even")
# else:
#     print("odd")    

#3.Write a program to check whether a given number is greater than 10 or not. if it is greater than 10 print message as greater or else print that number with not a greater than
# num=int(input())
# if num>10:
#     print(f"{num} is greater")
# else:
#     print(f"{num} is not a greater")  
#   
#4.WAP to check whether a given value is present in between 45 to 125. If value is present print the ascii character.
# num=int(input())
# if num>45 and num<125:
#     print(chr(num))
# else:
#     print("The value is not in between of 45 and 125")    

#5.WAP to check whether the given two input numbers are divisible by 3 and 5. If it is divisible, print “Good Morning”, if it is not print “Good Evening”.
# num1=int(input())
# num2=int(input())
# if num1%3==0 and num1%5==0 and num2%3==0 and num2%5==0:
#     print("Good Morning")
# else:
#     print("Good Evening")    

#6.WAP to accept two integers and check whether they are equal or not. If equal, multiply to value or quotation value and display it.
# n1=int(input())
# n2=int(input())
# if n1==n2:
#     p=n1*n2
#     q=n1//n2
#     print(p,q)
# else:
#     print("The numbers are not equal")    

#7.WAP to find the largest of two numbers.
# n1=int(input())
# n2=int(input())
# if n1>n2 :
#     print(f'{n1} is largest')
# else:
#     if n2>n1:
#         print(f'{n2} is larger')
#     else:
#         print("both are equal")      
# 

#8.WAP to check whether the input number is greater than 10 or not if it is greater than 10 print messages as greater with print that number. if that number is not greater than 10 print that number.  
# num=int(input())
# if num>10:
#     print(f"{num} is greater")
# else:
#     print(num)    

#9.WAP to the given number integer, if n is greater than 21,print the absolute difference between n and 21 otherwise print twice the absolute difference.
# num=int(input())
# if num>21:
#     diff=num-21
#     print(diff)
# else:
#     diff=2*(num-21)
#     print(diff)    
    
#10.WAP to find the smallest of two numbers.
# n1=int(input())
# n2=int(input())
# if n1<n2:
#     print(f'{n1} is smallest')
# else:
#     if n2<n1:
#         print(f'{n2} is small')
#     else:
#         print('both are equal')        

#11.WAP to check whether the given number is even or odd. If it is even then make it as an odd number, if it is an odd number then make it as even number.
# num=int(input())
# if num%2==0:
#     num=num-1
#     print(num)
# else:
#     num=num+1
#     print(num)    

#12.WAP to check whether the given number is divisible by 3 or not if yes,print the number or else print the cube of the numbers.
# num=int(input())
# if num%3==0:
#     print(num)
# else:
#     num=num**3
#     print(num)

#13.WAP to check whether the given input is divisible by 3 and 5. If yes print the actual number or else print string of that number.
# num=int(input())
# if num%3==0 and num%5==0:
#     print(num)
# else:
#     st=str(num)
#     print(st)   

# 14.WAP to check whether the given number lies between 1 to 19, if it is true square that number or else false cube that number and display the number. 
# num=int(input())
# if num>1 and num<19:
#     num=num**2
#     print(num)
# else:
#     num=num**3
#     print(num)    

#15.WAP to check whether the student has passed or failed. If the student got more than 40 marks, print ‘PASS’ along with those marks, if it is not printed ‘FAIL’ along with those marks
# num=int(input())
# if num>40:
#     print(f'{num} is PASS')
# else:
#     print(f'{num} is FAIL')    

#16.WAP to check whether a given value is even and in range of 47 to 58 and not in 0 or odd. if condition is True, to perform display the ascii character.or else to perform floor division with 5 and display it.
# num=int(input())
# if num%2==0 and num>47 and num<58  and num!=0:
#     num=chr(num)
#     print(num)
# else:
#     num=num//5
#     print(num)    

#17.WAP to check whether a given value is less than 125 and in between 47 to 125 or not. if condition is True, to perform store the given 
# value as key and value as a character into the dict.or else to append the value in list and display it.
# list=[]
# dict={}
# num=int(input())
# if num<125 and num>47 and num<125:
#     dict[num]=chr(num)
#     print(dict)
# else:
#     list.append(num)  
#     print(list)  
    
 #18.WAP to check whether a given character is in the alphabet or not. if alphabet, display the alphabet with character.or else display the not alphabet with character.
# char=input()
# asci=ord(char)
# if (asci>=65 and asci<=90) or (asci>=97 and asci<=122):
#     print(f"alphabet with {char}")
# else:
#     print(f"not alphabet with {char}")    


#19.WAP to check whether a given character is uppercase or other character. if uppercase, display the uppercase with character.or else display the other character with character.
# char=input()
# if char>='A' and char<='Z':
#     print(f'{char} is a Uppercase ')
# else:
#     print(f'{char} is not a uppercase')    

#20.WAP to check whether a given character is lowercase or other character. if lowercase, display the lowercase with character.or else display the other character with character.
# char=input()
# if char>='a' and char<='z':
#     print(f'{char} is a lowercase ')
# else:
#     print(f'{char} is not a lowercase')   

#21.WAP to check whether a given character is uppercase or other character. if uppercase, convert to lowercase .or else display the ascii number.
# char=input()
# if char>='A' and char<='Z':
#     char=chr(ord(char)+32)
#     print(char)
# else:
#     print(ord(char))    

#22.WAP to check whether the given character is in lowercase or uppercase. If it is in lowercase, convert it into uppercase, or else it is in uppercase and convert it into lowercase. Display the value.
# char=input()
# if char>='a' and char<='z':
#     char=chr(ord(char)-32)
#     print(char)
# else:
#     char=chr(ord(char)+32)
#     print(char)    

#23.WAP to check whether the given string of the first character is a special symbol or not. If a special symbol, to extract and display the middle character or else to reverse 
# the string and display the half of the string.
# st=input()
# first=st[0]
# if not ((first>='A' and first<='Z') or (first>='a' and first<='z') or (first>='0' and first<'9')):
#     mid=len(st)//2
#     print(st[mid])
# else:
#     res=st[::-1]
#     half=len(res)//2
#     print(st[:half])

#24.WAP to check whether the input character is a vowel or not. If it is vowel print ‘VOWEL’ along with that character, if it is not just print ‘CONSONANT’.
# char=input()
# if char in 'aeiouAEIOU':
#     print(f'{char} is VOWEL')
# else:
#     print('CONSONANT')    

#25.WAP to check whether a given character is a vowel or consonant. if vowel,to print the next character of a given character or else print previous characters.
# char=input()
# if char in 'aeiouAEIOU':
#     print(chr(ord(char)+1))
# else:
#     print(chr(ord(char)-1))    

#26.WAP to check whether a given string of first character is alphabet or not if the alphabet prints, reverse the string or else print the middle character.
# st=input()
# char=st[0]
# if (char>='A' and char<='Z') or (char>='a' and char<='z'):
#     rev = st[-1::-1]
#     print(rev)  
# else:
#     mid=len(st)//2
#     print(st[mid])      


#27.WAP to check whether the given input character is uppercase or lowercase. If the input character is upper case convert into lower case and vice versa.
# char=input()
# if char>='A' and char<='Z':
#     print(chr(ord(char)+32))
# else:
#     print(chr(ord(char)-32))    

#28. WAP to check whether a given string is less than 3 characters, to print the entire string otherwise to print after third positions to the remaining string.
# st=input()
# if len(st)<=3:
#     print(st)
# else:
#     print(st[3::])    

#29.WAP to check whether a given length of the string is even or not. if even, to append the new string called "bye" or else print the first and last characters.
# st=input()
# if len(st)%2==0:
#     new_st=st+'bye'
#     print(new_st)
# else:
#     print(st[0],st[-1])    


#30.WAP to check whether a given length of the string is odd or not. if odd, to append the new string("Haii") from the starting of the given string, or else to avoid the
#starting character and ending character of the given string and to display the remaining characters.
# st=input()
# if len(st)%2!=0:
#     new_st='Haii'+st
#     print(new_st)
# else:
#     new_st=st[1:len(st)-1]
#     print(new_st)    


#31.WAP to check whether the last of the given string is a special character or not, if the special character prints reverse the string except the last character or else to check
#if the length of the string is odd or not, if odd to extract the middle character to the end of the string.
# st=input()
# last=st[-1]
# if not ((last >= 'A' and last <= 'Z') or (last >= 'a' and last <='z') or (last>'0' and last<='9')):
#     res=st[-2::-1]+last
#     print(res)
# else:
#     len(st)%2!=0
#     mid=len(st)//2
#     mid_char=st[mid]
#     res=st+mid_char
#     print(res)

#32.WAP to check whether a given year is a leap year or not. if leap year, print leap year or else not a leap year.
# year=int(input())
# if(year%4==0 and year%100!=0) or (year%400==0):
#     print("leap year")
# else:
#     print('Not a leap year')    

#33.WAP to find out the greatest of two numbers and display the greatest number.if the greatest number, display the greatest message with value.
# n1=int(input())
# n2=int(input())
# if n1>n2:
#     print(f'{n1} is greater')
# else:
#     print(f'{n2} is greater')    


#34.WAP to check whether the given value is present inside the given collection or not.if value is present, display the value is available or else the value is not present.
# List=[10,20,30,40,23]
# num=int(input())
# if num in List:
#     print(f"The value {num} is available")
# else:
#     print(f"The value {num} is not present")    

#35.WAP whether a given string, if string length is more than 2, then it displays a new string with the first and last characters switched, otherwise the display 
#the 3 copies of given string.
# st=input()
# if len(st)>2:
#     res=st[-1]+st[1:-1]+st[0]
#     print(res)
# else:
#     print(st*3)    

#36.WAP to check whether a given value is a list and first and last values should be integer,if condition is satisfied first value is true division by 3 and perform the
#bitwise not for last value and those result values are stored in same positions in list or else, to perform length of the collection power 2 and display it.
# list1=list(map(int,input().split()))
# print(list1)
# if (type(list1)==list):
#     print(list1[0])


#37.WAP to check whether a given value is a string or not and length of the value should be more than 7, if condition is satisfied to append the new string in the middle of the
#given string or else to perform the replications with 3 and display the result.
# st=input()
# if type(st)==str and len(st)>7:
#     val=len(st)//2
#     res=st[:val]+'NEW'+st[val:]
#     print(res)
# else:
#     print(st*3)    

#38. WAP to check if the given string of first and second character should be sequence or not. if the sequence prints the first,second and last two characters, or else the first
#half string is reversed and the remaining half string should be normal and display it.
# st=input()
# if ord(st[1]) == ord(st[0])+1:
#     res=st[0]+st[1]+st[-2]+st[-1]
#     print(res)
# else:
#     half=len(st)//2
#     res=st[:half][::-1]+st[half:]
#     print(res)    

#39.WAP to check whether a given value is present inside the collection or not. If present, print the value or else print value is not found.
# List=[10,20,30,40,50,60]
# st=int(input())
# if st in List:
#     print(st)
# else:
#     print("value is not found")    


#40.WAP to check whether a given key is present in the dict or not. if key is present: display the value or else add key and new value inside the dict.
# d={'a':10,'b':20,'c':30}
# key=input()
# if key in d:
#     print(f"{key}:{d[key]}")
# else:
#     value=input()
#     d[key]=value
#     print(d)


#41.WAP to check whether a given collection is set or not.if set, append the new value, or else eliminate the duplicate values 
# in collection. final results should be set type.



#42.WAP to read the age of a candidate and determine whether it is eligible for his/her own vote or not.it eligible print age and eligible messages or else print not eligible.
# age=int(input())
# if age>18:
#     print(f"{age} is eligible for vote")
# else:
#     print("not eligible to vote")    


#43.WAP to check whether a given value is even and in between 47 to 58 and not in 0 or odd. if condition is True, to perform display the ascii character.
#or else to perform floor division with 5 and display it.
# value=int(input())
# if (value%2==0) and (value>47 and value<58):
#     print(chr(value))
# else:
#     print(value//5)


#44.WAP to check whether the given string is palindrome or not if it is a palindrome string palindrome along with the string if it is not a palindrome print not palindrome
# st=input()
# if st==st[::-1]:
#     print(f"palindrome {st}")
# else:
#     print("Not a palindrome")    

#45.WAP to check whether a given number is palindrome or not. If palindrome, display the given value as a palindrome or else not a palindrome.
# num=input()
# if num == num[::-1]:
#     print(f"{num} is palindrome")
# else:
#     print("Not a palindrome")       


#46.WAP to check length of both string collections equal or not if both are equal print the concat the two strings and display, or else if any one 
#of the collection not equal print both the collections with lengths


#47.WAP to check whether both given values point to the same memory location or not. if it is true print the middle item of the second collection, 
#or else if it is false print the first item and last item of the first collection along with the memory address.


st=input()
print(st.lower())
print(st.upper())