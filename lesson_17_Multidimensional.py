print("Multidimensional Sequences Test")

myTableList = [[1,2,3], [4,5,6], [7,8,9]]

print("Value in table list")
for row in myTableList:
    for item in row:
        print(item, end=" ")
    print()


print()
myTableTuple = ( (1, 2, 3), (4, 5, ), (6, 7, 8))
for row in myTableTuple:
    for item in row:
        print(item, end="")
    print()



def printList(inputList):
    print("Value in List: ")
    for row in inputList:
        for item in row:
            print(item, end=" | ")
        print()

def average(gradesOfStudent):
    total = 0.0
    for grade in gradesOfStudent:
        total += grade
    return total/len(gradesOfStudent)


print()
listOfGrades = [ [6.4, 7.5, 8.2, 7.7], [9.8, 8.8, 8.9, 9.1], [8.2, 9.0, 8.6, 8.7], [6.1, 3.2, 0.0, 7.1]]

printList(listOfGrades)

for i in range(len(listOfGrades)):
    print("Average / Student ", i, "is ", average(listOfGrades[i]))


