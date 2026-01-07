class Employee:
    empId = 1
    def __init__(self):
        print("Employee class")

class Programmer(Employee):
    empId = 2
    def __init__(self):
        super().__init__()
        print("programmer class")

class Manager(Programmer):
    empId = 3
    def __init__(self):
        super().__init__()
        print("manager class")

o = Manager()
print(o.empId)