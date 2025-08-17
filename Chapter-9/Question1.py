# 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f = open("file.txt");

data = f.read();

if("twinkle" in data):
    print("twinkle is present in the content"
    )
else:
    print("not present")
f.close()


