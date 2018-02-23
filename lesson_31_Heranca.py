class Person:

    def __init__(self, name, last):
        self.firstname = name
        self.lastname = last

    def getName(self):
        return self.firstname + " " + self.lastname


class Employee(Person):

    def __init__(self, first, last, employeeId):
        Person.__init__(self, first, last)
        self.employeeId = employeeId

    def getEmployee(self):
        return self.getName() + " " + self.employeeId


x = Person("Everton", "Kluczkovski")

y = Employee("Clara", "Klucz", "107")

print("Initial program...")
print("")
print(x.getName())
print(y.getEmployee())

