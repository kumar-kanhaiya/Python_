math = int(input("Enter math marks : "))
English = int(input("Enter English marks : "))
Science = int(input("Enter Science marks : "))

average = (math+ English + Science)/3;
# print(average)
if(average >=90 and average<=100):
    print("Excellent")

elif(average>=80 and average<90):
    print("A");

elif(average>=70 and average<80):
    print("B")

elif(average>=60 and average<70):
    print("C")

elif(average>=50 and average<60):
    print("D")
else:
    print("Fail")
