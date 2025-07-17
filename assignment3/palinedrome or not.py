num=int(input("enter the three digit number"))
copy=num#123
a=num%10#3
num=num//10#12
b=num//10#1
c=num%10#2
reverse=(a*100+c*10+b)
if(copy==reverse):
    print("It is palinedrome")
else:
    print("It is not palinedrome")    
