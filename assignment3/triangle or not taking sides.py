a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the third side"))
if((a+b)>c and (b+c)>a and (a+c)>b ):
    print("It is triangle")
else:
    print("It is not triangle")    