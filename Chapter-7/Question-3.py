number = int(input("Enter your number : "))
check = True;

for i in range(2,number):
    if(number %i == 0):
        check = False;
if(number < 0):
    print("this is not prime ")
elif(check):
    print("This is prime number ")

else:
    print("This is not a prime ")
