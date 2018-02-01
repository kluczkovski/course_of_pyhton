print("Dictionary Test")

mydictionaryHeight = {"Everton": 1.86, "Alana": 1.60, "Fabiano": 1.95, "Clara": 0.58}

print(mydictionaryHeight)
print("Everton's height:", mydictionaryHeight.get('Everton'))
print("Clara's height:", mydictionaryHeight.get('Clara'))

print()
mydictionaryHeight["Clara"] = 0.065
print("Clara's height:", mydictionaryHeight.get('Clara'))


print()
mydictionaryHeight["Guga"] = 1.76
print(mydictionaryHeight)

del mydictionaryHeight["Fabiano"]
print(mydictionaryHeight)


# Implementation histogram

print("\n\n\n")
print("Histogram Test")


def histogram(text):
    myDictionary = dict()
    for c in text:
        if c not in myDictionary:
            myDictionary[c] = 1
        else:
            myDictionary[c] +=1

    return myDictionary

def print_histogram(dictionary):
    for c in dictionary:
        print(c, "=", dictionary[c])

result = histogram("Devmedia is a great company to learn programming")
print(result)

print()
print_histogram(result)