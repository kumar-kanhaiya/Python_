math = int(input("Enter math marks : "))
English = int(input("Enter English marks : "))
Science = int(input("Enter Science marks : "))

average = (math+ English + Science)/3;

if(average >=40 and math>=33 and English>= 33 and Science>=33):
    print("Beta Pass ho Enjoy !!")

else:
    print("Try again you are fail !!")