# for loops
# range is function generate seq of number 
# range(start,stop)
for i in range(1,6):
    print("aniket")

# range(start,stop,step_size)
for i in range(1,10,2):
    print(i)

# range(0,3) you can write range(3)
for i in range(3):
    print("salunkhe")

# we can print list in loop
list = [1,2,45,18,"aniket"]
for i in list:
    print(i)


# we can print tupler in loop
tuple = (1,2,45,18,"aniket",18,45)
for i in tuple:
    print(i)

# break statement
for i in range(5):
    if(i==3):
        break 
    print(i)
    i+=1

# continue statement
for i in range(5):
    if(i==3):
        continue 
    print(i)
    i+=1