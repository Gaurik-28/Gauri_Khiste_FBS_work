three_digit_number=float(input("enter the three digit number"))
num=(three_digit_number//10)
third_digit=num%10
first_digit=num//10
second_digit=num%10
if((first_digit==2*second_digit) and (first_digit==0.5*third_digit)):
    print("yes,you have done it")
else:
    print("please try next time")    

