print("Test if / else")

velocity  = input("Enter your velocity: \n")
velocity = int(velocity)

if velocity > 100 :
    print("Too fast!!!")

else:
    print("Your velocity is ok!!!")

print("Finished velocity...")


grade = input("\n Enter your grade: \n")
grade = int(grade)

if grade >=9:
    print("your grade is A")
    print("Congratulation!!!")
elif grade >=8:
    print("your grade is B")
    print("Good!!!")
elif grade >=7:
    print("your grade is C")
    print("Maybe")
elif grade >=6:
    print("your grade is D")
    print("bad")
else:
    print("you will try again!!!")

print("The End")