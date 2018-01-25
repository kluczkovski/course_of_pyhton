print("\nLoop - While \n")

total = 0


#while total <=100 :
#    print("%d loop interaction" %total )
#    total +=1


factorial_number = input("Enter with number:")
factorial_number = int(factorial_number)

# factorial 4 = 4 * 3 * 2 * 1


if factorial_number > 0 :
    step = factorial_number
    total = factorial_number
    while step > 1 :
        step -=1
        total = total * step
    print("The factorial of %d is %d" % (factorial_number,total))

elif factorial_number == 0:
    print("The factoria of 0 is 1")

else:
    print("Not exist factorial of negative number")


print("THE END")
