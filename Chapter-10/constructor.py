class Employee:
    language = "python"
    salary = 120000

    def __init__(self , name , salary , language): # dunder method which is automatically called 
        self.name = name;
        self.salary = salary;
        self.language = language
        print("Creating new object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def great():
        print("Good morning")    

kanhaiya = Employee("kanhaiya",125000,"java");
kanhaiya.getInfo()
kanhaiya.great()        

