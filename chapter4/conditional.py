# enter age and print conditional messages

age = int(input("Enter your age: "))

if(age>=18):
    print("your age is valid for voting")

elif(age<0):
    print("Enter valid age")

else:
    print("your are under age for voting")

print("Thank you")
