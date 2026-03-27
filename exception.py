# n1=int(input())
# n2=int(input())
# res=n1//n2
# print(res)

# n=int(input())
# print(n)

# a=0.99
# st=eval(input())
# print(st,type(st))

#n1=int(input())
# n2=int(input())
# try:
#     res=n1//n2
#     print(res)
#     print('fine')
# except ZeroDivisionError:
#     print("zero should not be in denominator")    
# print("Finally") 


def greet():
    def message():
        print("hello")
    message()
# greet()

def calculate():
    def add(a, b):
        return a + b
    def multiply(a, b):
        return a * b

    x = add(3, 4)
    y = multiply(3, 4)
    print("Addition:", x)
    print("Multiplication:", y)

# calculate()


def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func  # returning inner function

add_10 = outer_func(10)
print(add_10(5))



def atm(pin):
    def withdraw(amount):
        print(f"✅ Withdrawn ₹{amount} successfully.")
    def check_balance():
        print("💰 Your balance is ₹10,000.")
    
    if pin == 1234:
        print("Access Granted ✅")
        withdraw(2000)
        check_balance()
    else:
        print("❌ Wrong PIN!")

atm(1234)
