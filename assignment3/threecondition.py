print("1.area of rectangle")
print("2.check the even or odd num")
print("3.cube of the num")
option=int(input("enter the option"))
if(option==1):
    l=int(input("enter the length"))
    b=int(input("enter the breadth"))
    area=l*b
    print("area of rectangle",area)
elif(option==2):
    num=int(input("enter the number"))  
    if(num%2==0):
        print("number is even")  
    else:
        print("number is odd")    
else:
    num=int(input("enter the number"))  
    cube=num**3
    print("The cube of number",cube)      

