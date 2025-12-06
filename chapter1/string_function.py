# Change
name = "aniketsalunkhe"
# length of string
print("length-", len(name))

# return bool string start with (Case sensitive)
print("starts with-", name.startswith("ani"))

# return bool string ends with (Case sensitive)
print("ends with-", name.endswith("et"))

# capitalize only starting char
print("capitalize-", name.capitalize())

# title
print("title-", name.title())

# upper
print("upper-", name.upper())

# lower
print("lower-", name.lower())

# swapcase
print("swapcase-", name.swapcase())

# find --return index of char  or -1
print("find -",name.find("a"))

#index return index of char other wise error
print("index-", name.index("i"))

# replace
print("replace-",name.replace("aniket","maya"))

# string split -convert to array
print("string split-", name.split(" "))

# join
namesplit = name.split(" ")
print("string join-"," ".join(namesplit))
 
# strip lstrip(left) rstrip(right)
print(name.strip())

# checktype
# only letters is there is space still return false
print("isaplha-",name.isalpha())

# only number
print("isdigit -","123".isdigit())

# letters + number
print("isalnum-",name.isalnum())