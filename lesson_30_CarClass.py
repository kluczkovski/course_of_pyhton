class Car:

    def __init__(self, automaker, model):
        self.automaker = automaker
        self.model = model


    def __getattr__(self, name):
        return "Not Exist"


    def __setattr__(self, name, value):
        if name == "automaker":
            if value == "GM":
                self.__dict__["automaker"] = "Chevrolet"
            else:
                self.__dict__["automaker"] = value
        else:
            self.__dict__[name] = value

    def __delattr__(self, name):
        print("Attribute was Deleted")

print("")
myCar = Car("Ford","Focus")
print(myCar.model)
print(myCar.automaker)
print(myCar.year)

print("")
myCar2 = Car("GM", "CELTA")
print(myCar2.model)
print(myCar.automaker)