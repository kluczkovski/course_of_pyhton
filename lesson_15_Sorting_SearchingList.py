print("Sorting and Searching list")

myList = [34, 5, 2, 85, 99, 15, 1, 74, 85, 93, 44, 7, 69, 1, 85]

print("\nItems in original order:")
for item in myList:
    print(item)


myList.sort()
print("\nItens sort list")
for item in myList:
    print(item)

myList.reverse()
print("\nItens reverse list")
for item in myList:
    print(item)

print("Size of list is: ", len(myList))
print("Count of variable 85", myList.count(85))


print()

myStringList = ['Everton', 'Alana', 'Clara', 'Python', 'Alana']

print(myStringList)

searchName = input("Type a string to be find:\n")

if searchName in myStringList :
    print("Found at index: ", myStringList.index(searchName))
else:
    print("Not found!")