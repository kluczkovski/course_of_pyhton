class Rectangle:

    resultArea = 0

    def __init__(self, sideA = 1, sideB = 1):

        self.calcArea(sideA, sideB)

    def calcArea(self, sideA, sideB):
        self.resultArea = sideA * sideB


myRectangel = Rectangle()
print("\nThe result area is " + str(myRectangel.resultArea))


myRectangel2 = Rectangle(2,2)
print("\nThe result area is " + str(myRectangel2.resultArea))
