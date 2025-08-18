class Employee:
    language = "python"
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def great():
        print("Good morning")    

kanhaiya = Employee();
kanhaiya.getInfo()
kanhaiya.great()        

