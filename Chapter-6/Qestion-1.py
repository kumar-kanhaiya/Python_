a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))
c = int(input("Enter your third number : "))
d = int(input("Enter your fourth number : "))

if(a>=b and a>=c and a>=d):
    print(a , " is the greatest number")

elif(b>=a and b>=c and b>=d):
    print(b , " is the greatest number")
    
elif(c>=a and c>=b and c>=d):
    print(c , " is the greatest number")
    
else:
    print(d , " is the greatest number")
    
