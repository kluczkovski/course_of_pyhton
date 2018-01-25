print("Test format strings")

myInteger = 12345
myFloat   = 3.14155
myString = "Devmedia is a great company"

print("Integer", myInteger)

print("Decimal is %d  and my integer is %d " % (myFloat, myInteger))

print("Hexadecimal integer %x" %myInteger)

print("String", myString)

print("Float", myFloat)
print("Default %f" %myFloat)
print("Exponential %e" %myFloat)
print("Right justify (%10d)" %myFloat)
print("Left justify (%-10d)" %myFloat)

print("Force nine digits %.9d" %myInteger)
print("Three digits after decimal in float %.3f" %myFloat)
print("Ten and five characters allowed in string:")
print("(%.10s) (%.5s)" % (myString, myString))
