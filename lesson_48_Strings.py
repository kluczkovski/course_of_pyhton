myString_01 = "A, B, C, D, F,"


print("\nString is %s" % myString_01)
print("Split string by spaces: ", myString_01.split())
print("Split string by commas: ", myString_01.split(","))
print("Split string by commas, max 2", myString_01.split(",", 2))
print()

myList_01 = ["A", "B", "C", "D", "E", "F", "G"]
myString_02 = "-"

print("List is ", myList_01)
print("Joining with -> %s: is %s" %(myString_02, myString_02.join(myList_01)))
print("Joining with -> .-. is ", ".-.".join(myList_01))
print()

string_text = "Everton Kluczkovski is a developer. All developer are crazy"
print(' "developer" occurs %d times in \n\t%s' %(string_text.count("developer"), string_text))
print()

string_text_2 = "My dog is angry"
print(' "%s" contains "dog" starting at index %s' %(string_text_2, string_text_2.find("dog")))
print()

try:
    print(' "angri" index is ', string_text_2.find("angri"))
except ValueError:
    print(' "angri" does not occur in "%s"' %string_text_2)
finally:
    print()


if string_text_2.startswith("My"):
    print(' "%s" starts with "My" ' %string_text_2)
    print()

if string_text_2.endswith("My"):
    print(' "%s" ends with "My" ' %string_text_2)
    print()


print('Index from first string of "developer" in "%s" is %d' %(string_text, string_text.find("developer")))
print('Index from last string of "developer" in "%s" is %d' %(string_text, string_text.rfind("developer")))
print()

string_text_3 = "never say never"
print("Original: ", string_text_3)
print('Replaced "never" with "forever": ', string_text_3.replace("never","forever"))
print('Replaced 1 maximum: ', string_text_3.replace("never","forever", 1))
print()




