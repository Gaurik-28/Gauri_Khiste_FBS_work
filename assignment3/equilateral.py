side1=int(input("enter the first side"))
side2=int(input("enter the second side"))
side3=int(input("enter the third side"))
if(side1==side2==side3):
    print("It is equilateral triangle")
elif(side1==side2 or side2==side3 or side1==side3):
    print("it is isoscaleous triangle")
else:
    print("it is scalar triangle")

        