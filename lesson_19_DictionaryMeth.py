print("Dictionaries Methods Test")

myMonthsDictionary = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July",
                      8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}


print("\nThe myMonthsDictionary items are: ", myMonthsDictionary.items())
print("\nThe myMonthsDictionary keys are: ", myMonthsDictionary.keys())
print("\nThe myMonthsDictionary values are: ", myMonthsDictionary.values())

myInput = input("Enter with your birthday month:")
myInput = int(myInput)

if myInput in myMonthsDictionary:
    print("Your birthday month is ", myMonthsDictionary.get(myInput))
else:
    print("Not exist this month")


newMonthDictionary = myMonthsDictionary.copy();

print(newMonthDictionary)
print(myMonthsDictionary)

newMonthDictionary[3] = "nothing"
print(newMonthDictionary)

newMonthDictionary = {0:"Nothing", 13:"out of range"}
print(newMonthDictionary)

myMonthsDictionary.update(newMonthDictionary)
print(newMonthDictionary)
print(myMonthsDictionary)

