# dictionory is mutable

marks = {
    "aniket":100,
    "rahul":45,
    "rohit":99
}

print(marks)

# update dict (given dict key present in original dict then updated else add) 
marks.update({"rohit":98,"sachin":100})
print(marks)

# get keys from dict
print(marks.keys())

# get values from dict
print(marks.values())

# get particular value if key not present give error
print(marks["sachin"])

# get particular value if key not present return none
print(marks.get("sachin2"))

# remove item
marks.pop("rohit")
print(marks)

# remove lastitem
marks.popitem()
print(marks)

print(marks.items())