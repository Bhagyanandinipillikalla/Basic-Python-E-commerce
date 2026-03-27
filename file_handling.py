# f1=open('demo.txt','r')
# print(f1.read())
# f1.close()


# s=open('demo.txt','w')
# s.write('Hello')
# s.close()

# a=open('demo.txt','a')
# a.write(' Welcome to python')
# a.close()
# b=open('demo.txt','r+')
# print(b.read())
# b.write('in filehandling')
# b.close()

# m=open('demo.txt','w+')
# m.write(' byee byee')
# m.seek(0)
# print(m.read())
# m.close()


# try:
#     with open('data.txt','r') as f:
#         lines=f.readlines()
#         total=len(lines)
#         total_words=sum(len(line.split()) for line in lines)

#         print(total)
#         print(total_words)
# except FileNotFoundError:
#     print('File does not Exist')        


# n=open('text.txt','w')
# n.write("Bhagya Nandini")
# n.close()


# data=b'Hello world'       # b'Hello World' means bytes, not string.
# with open('sample.bin','wb') as f:
#     f.write(data)


# with open('sample.bin', 'rb') as f:
#     content = f.read()
# print(content)



# try:
#     with open(r"C:\Users\pbhag\OneDrive\Desktop\photo1.png",'rb') as f:
#         data=f.read()
#         print(data)
#         with open('newimg.jpg','wb') as file:
#             file.write(data)
# except Exception as e:
#     print(e)      

import csv
# try:
#     with open('demo.csv','w',newline='') as f:
#         w=csv.writer(f)
#         header=['name','age','address']
#         w.writerow(header)
#         w.writerow(['rani','22','Goa'])
#         students=[
#             ['nandu','22','Tirupati'],
#             ['Bhagya','23','chittor']
#         ]         
#         w.writerows(students)
#     with open('demo.csv','r') as file:
#         f1=csv.reader(file)
#         for i in f1:
#             print(i)
# except Exception as e:
#     print(e)                

# with open("demo.csv", "a", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Sita", 24, "Hyderabad"])



# try:
#     with open('dict.csv','w',newline='') as file:
#         fieldnames=['name','age','address']
#         f=csv.DictWriter(file,fieldnames)
#         f.writeheader()
#         f.writerow({'name':'rani','age':'22','address':'goa'})
#         f.writerow({'name':'Bhagya','age':'23','address':'Tirupati'})
#     with open("dict.csv", "r") as f1:
#         reader = csv.DictReader(f1)
#         for row in reader:
#             print(row)    
# except Exception as e:
#     print(e)


# import csv
# try:
#     with open('students.csv','w',newline='') as file:
#         file1=csv.writer(file)
#         header=['roll','name','age','marks']
#         file1.writerow(header)
#         file1.writerows([
#             ['101','rani',20,324],
#             ['102','manu',21,234],
#             ['103','nani',21,321],
#             ['104','gani',21,225],
#             ['105','vani',21,421]
#         ])

#     with open('students.csv','r') as f1:
#         file2=csv.reader(f1)
#         next(file2)
#         for i in file2:
#             if int(i[2])>20:
#                 print('\t'.join(i)) 

#     with open('students.csv','r') as f2:
#         reader=csv.reader(f2)
#         header=next(reader)
#         print(header)

#     with open('students.csv','r') as f3:
#         read=csv.reader(f3)
#         next(read)
#         c=0
#         for i in read:
#             c+=1
#         print(c) 

#     with open('students.csv','a',newline='') as files:
#         writer=csv.writer(files)
#         writer.writerow(['106','malani','23',435])

# except Exception as e:
#     print(e)               


import csv
with open('marks.csv','w',newline='') as file:
    file1=csv.writer(file)
    file1.writerow(['rollno','name','marks'])
    file1.writerows([
        [101,'bhagya',67],
        [102,'nandini',72],
        [103,'manu',84],
        [104,'ravi',82],
        [105,'meena',56]
    ])
    total=0
with open('marks.csv','r') as sheet:
    reader=csv.reader(sheet)
    next(reader)
    for i in reader:
        total+=int(i[2]) 
print(total)           