class Pet:

    def __init__(self, name, specie):
        self.name = name;
        self.specie = specie


    def getName(self):
        return self.name

    def getSpecie(self):
        return  self.specie

    def __str__(self):
        return "%s is a %s" %(self.name, self.specie)


myPet1 = Pet("Pepita", "dog")
myPet2 = Pet("Hanna", "cat")
myPet3 = Pet("Snow", "human")

print("")
print("")
print(myPet1)
print(myPet2)
print(myPet3)

print("")
print("myPet1 name attribute: " + str(myPet1.specie))
print("myPet1 name attribute: " + str(myPet1.getSpecie()))
print("myPet2 name attribute: " + str(myPet2.getName()))
print("myPet3 name attribute: " + str(myPet3.getSpecie()))
