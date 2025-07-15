num=int(input("enter the number"))
reverse=0
while(num!=0):
    a=num%10
    num=num//10
    reverse=(reverse*10)+a
print(reverse)    