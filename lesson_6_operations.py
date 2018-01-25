print("Test Equality and Relational Operators")

number1 = input("Enter first number \n")
number1 = int(number1)

number2 = input("Enter second number \n")
number2 = int(number2)

if (number1 == number2):
    print("%d is equal to %d" %(number1, number2))
    print("equal")

if (number1 != number2):
    print("%d is not equal to %d" %(number1, number2))
    print("not equal")

if (number1 < number2):
    print("%d is less than %d" % (number1, number1))

if (number1 > number2):
    print("%d is more than %d" % (number1, number2))