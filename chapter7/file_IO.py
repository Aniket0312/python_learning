# open read file default is r parameter
# file = open(r"C:\ISG\Work\Aniket\Python_Learning\test.txt")
file = open("file.txt")
filetext =file.read()
file.close()
print(filetext)

# readlines return lines of list
# file = open("file.txt")
# filetext =file.readline()
# while(filetext!=""):
#     print(filetext)
#     filetext = file.readline()



# file.close()

# write file w is  parameter stands for write
# file = open("sample.txt","w")
# file.write("this is write sample file")
# file.close()