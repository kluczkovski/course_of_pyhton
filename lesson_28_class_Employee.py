class Employee:

    employeeCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employeeCount += 1

    def showEmployee(self):
        print("\nName: ", self.name, ", Salary: ", self.salary)

    def showCount(self):
        print("\nQuantity of Employees is %d " % Employee.employeeCount)