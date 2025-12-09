# function syntax
# average logic

# this are user defined function
# function defination
def average():
    a = int(input("Enter number "))
    b = int(input("Enter number "))
    c = int(input("Enter number "))
    avg = (a+b+c)/3
    print(avg)

# function call
# average()

def GreetUser(userName,ending):
    print("Good day, "+userName)
    print(ending)

#GreetUser("aniket","thank you")
#GreetUser("advik","thank you")
#GreetUser("rahul","thank you")

# Built in function
# print(),len(),range()

# return value
def muliple(num1,num2):
    return num1 * num2

ans=muliple(12,5)
print(ans)