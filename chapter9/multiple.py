class Employee:
    company ="ISG E Solutions"

    def __init__(self,designation):
        self.designation = designation

    def getDesignation(self):
        print(f'designation of employee is {self.designation}')

class Coder:
    company ="FreeLancer"
    language = "python"

    def showLanguage(self,):
        print(f'known language are {self.language}')

class Programmer(Employee,Coder):
    company = "ITC"
    def __init__(self,designation):
        self.designation = designation

o = Employee("support")
print(o.company)
o.getDesignation()

o = Programmer("software developer")
print(o.company)
o.getDesignation()
o.showLanguage()