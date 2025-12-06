# elements not repeat in set
s = {1,2,4,5, 5 }

print(s)
# empty set
e = set()
# print(type(e)) # dont use e= {} it will create empty dict

# add methods
s.add(12)
print(s)

# update 
s.update([5,6])
print(s)

# return length
print(len(s)) 

# union intersection
u = {1,2,3,4,5,6,7}
w = {5,6,7,8,9,0}

# union unique value from both sets
print(u.union(w))

# intersection - overlapping values from both set
print(u.intersection(w))


