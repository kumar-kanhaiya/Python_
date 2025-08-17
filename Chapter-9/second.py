
f = open("file.txt")

lines = f.readlines()

print(lines , type(lines))

f.close()

# the same can be written using with statement 
# like this :

with open("file.txt") as f:
    print(f.read())

#  you dant have to explicitly close the file 

