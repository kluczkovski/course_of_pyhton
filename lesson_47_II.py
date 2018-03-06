class Error(Exception):
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass


number = 5

while True:

    try:
        i_num = int(input("Digite a number:"))
        if i_num > number:
            raise ValueTooLargeError
        elif i_num < number:
            raise ValueTooSmallError
        break
    except ValueTooLargeError:
        print("Value is to Large. Try again!")
        print()
    except ValueTooSmallError:
        print("Value is to Small. Try again!")
        print()

print("Congratulations. Value is Correct")