number_01 = input("\nEnter numerator: ")
number_02 = input("\nEnter denominator: ")

try:
    number_01 = int(number_01)
    number_02 = int(number_02)
    result = number_01/number_02

except ValueError:
    print("Error: numbers only")

except ZeroDivisionError:
    print("Error: Divide by zero!")

else:
    print("Result of " + str(number_01) + " / " + str(number_02) + " is " + str(result))

finally:
    print("The program has ended!!!")