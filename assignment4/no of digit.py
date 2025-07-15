num=int(input("enter the number"))
count=0
while(num!=0):
    a=num%10
    num=num//10
    count=count+1
print(count)    