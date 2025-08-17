# Write a recursive function to calculate the sum of first n natural numbers.


def ans(number):
    if(number == 1):
        return 1
    
    return number + ans(number-1);


print(ans(10))