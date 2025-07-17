per=float(input("enter the percentage:"))

if(per>=80 and per<=100):
    print("first class with distinction")

elif(per>=70 and per<80):
    print("first class")

elif(per>=60 and per<70):
    print("higher secondary class")  

elif(per>=40 and per<60):
    print("secondary class")

elif(per<40 and per>=0):
    print("fail")
else:
    print("wrong input")              