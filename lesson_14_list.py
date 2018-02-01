print("Test List")

mylist = [54, 23, 89, 45, 12, 30, 98, 77, 29, 61]

print("Position 0: ", mylist[0])
print("Position 1: ", mylist[1])
print("Position 2: ", mylist[2])
print("Position 3: ", mylist[3])
print("Position 4: ", mylist[4])
print("Position 5: ", mylist[5])
print("Position 6: ", mylist[6])
print("Position 7: ", mylist[7])
print("Position 8: ", mylist[8])
print("Position 9: ", mylist[9])

print("Lengh of my list: ", len(mylist))

i = len(mylist)-1

while i >= 0 :
    print("Position ", i, " has ", mylist[i])
    i -=1;

print("Diferent way...")
for y in range(len(mylist)):
    print("Position ", y, " has ", mylist[y])


print()

myNewList = []
myNewList.insert(0, 'everton')
myNewList.insert(3, 'osmar')
myNewList.insert(2, 'alana')
myNewList.insert(1, 'mae')

print("Position 0 ", myNewList[0])
print("Position 1 ", myNewList[1])
print("Position 2 ", myNewList[2])
print("Position 3 ", myNewList[3])



