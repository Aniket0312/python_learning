lstnames =  ["aniket","mayur","rohit","rahul"]

# list is mutable unlikely string is immutable

# add name in list , append always add in last
lstnames.append("devendra")

# printing list
print(lstnames)

lstnum = [1,18,45,17,99,10,7]

# sort list in asc order
lstnum.sort()

# sort list in desc order
lstnum.sort(reverse=True)
print(lstnum)

# reverse list
lstnum.reverse()

# insert value at particular index
lstnum.insert(2,55)

lstnum = [1,18,45,17,99,10,7]
# remove value from list - return value
popvalue = lstnum.pop(3)
print(popvalue)

# remove value from list
lstnum.remove(7)


# find index from value - return value
indexval  = lstnum.index(18)
print(indexval)
print(lstnum)

# copy list 
lstcopy = lstnum.copy()
print(lstcopy)

# length of list
print(len(lstcopy))

# Clear list
lstnum.clear()