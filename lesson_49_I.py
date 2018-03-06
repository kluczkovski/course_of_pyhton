import re

# Example 1, using FINDALL
print()
myText = 'Bats are rats with wings'
print('Example 01 : my text is "%s"' %myText)
searchObj = re.findall(r'[b|r]ats', myText, re.MULTILINE | re.IGNORECASE)
if searchObj:
    print("Found: ", searchObj)
else:
    print("Not Found...")


# Example 2, using search
print()
value = "Developers are developers"
print('Example 02 : my text is "%s"' %value)
mySearch = re.search("(lope.*) (deve.*)", value, re.IGNORECASE)
if mySearch:
    print("Result of my search (group1): ", mySearch.group(1))
    print("Result of my search (group1): ", mySearch.group(2))
else:
    print("Not Found")

# Example 3, using match
print()
print('Example 02 : my text is "%s"' %value)
myMatch = re.match("(lope.*)", value, re.IGNORECASE)
if myMatch:
    print("Result is: ", myMatch)
else:
    print("Not found")

# Example 4, email validation
print()
inputEmail = input("\nEnter with your email:")
myDomian = re.search("@[\w.]+", inputEmail)
if inputEmail:
    print("The domian is: ", myDomian.group())
else:
    print("email is not valid")
