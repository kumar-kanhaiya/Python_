class Employee:
    company = "itc"
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


#  use of inheritance 

class programmer(Employee):
    company = "itc infotech "
    def show(self):
        print(f"the name is {self.name} and the salary is {self.salary}")


# child inherit all properties of parent 
