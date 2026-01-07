class Employee:
    company ="ISG E Solutions"

    def __init__(self,designation):
        self.designation = designation

    def getDesignation(self):
        print(f'designation of employee is {self.designation}')

class Programmer(Employee):
    company = "ITC"
    def __init__(self,designation):
        self.designation = designation

o = Employee("support")
print(o.company)
o.getDesignation()

o = Programmer("software developer")
print(o.company)
o.getDesignation()