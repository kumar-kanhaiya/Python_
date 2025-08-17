# Write a program using functions to find greatest of three numbers

def gretest(a,b,c):
    if(a>b and a> c):
        print(f"{a} is greatest ")
        
    if(b>a and b> c):
        print(f"{b} is greatest ")
    else:    
        print(f"{c} is greatest ")

gretest(2,5,9)