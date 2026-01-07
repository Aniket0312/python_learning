class Employee:
    designation = "developer"
    salary = 120000 #instance attribute

    #constructor- set values from constructor
    def __init__(self,name):
        self.name = name

    #self parameter use for instance of clss
    def getSalary(self):
        print(self.salary)

    #differece between normal & static method is self parameter
    #if we don't want to use self parameter then we create static method

    @staticmethod #decorator to mark static method
    def welcome():
        print("welcome user")
    

aniket = Employee("aniket") # object Instatiation
print(aniket.name,aniket.designation,aniket.salary)

aniket.salary = 20000 #changing class attribute
print(aniket.name,aniket.designation,aniket.salary)

rahul = Employee("rahul")
rahul.welcome()
print(f"{rahul.name} salary")
rahul.getSalary()
