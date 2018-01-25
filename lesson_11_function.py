print("Test Functions")

def factorial(n):

    if (n == 1):
        return 1
    else:
        result = n * factorial(n-1)
        print ("intermediate result for ", n, ":", result)
        return result

def sum(arg1, arg2):
    total = arg1 + arg2
    print("This print is inside function:", total)
    return total

total_soma1 = sum(100,115)

total_soma2 = sum(7,1000)

print(total_soma1)
print(total_soma2)
print(sum(10,30))


number = input("Type the number:")
number = int(number)

print("Final result is :", factorial(number))


