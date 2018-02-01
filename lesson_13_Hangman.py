import time
import random

name = input("What is your name? \n")
print("Hello " + name + " Time to play Hangman! \n")

time.sleep(1)

print("Start guessing...")

time.sleep(0.5)

print("...")

listOfWords = ("devmedia", "secret", "cat", "trash", "python")


randonNumber = random.randint(0, len(listOfWords) -1)
word = listOfWords[randonNumber]
guesses = ''
turns = 10

while turns > 0:
    failed = 0

    for char in word:

        if char in guesses:
            print(char)
        else:
            print("_")
            failed +=1;

    if failed == 0 :
        print("\n You win!!!")
        break
    print()


    char = input("Guess a character: \n")
    guesses += char

    if guesses not in word:
        turns -=1
        print("Wrong \n")
        print("You have ", turns, " more guesses")

        if turns == 0 :
            print("You loose \n")





print("The End!!!")