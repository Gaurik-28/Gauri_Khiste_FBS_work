start=int(input("enter the number"))
stop=int(input("enter the number"))
for i in range(start,stop+1):
    temp=i
    count=0
    while(i!=0):

        i=i//10
        count=count+1
    i=temp
    sum=0
    while(i!=0):
        a=i%10
        i=i//10
        sum=sum+(a**count)
if(sum==temp):

    print("yes,it is a armstrong number")
        
else:
    print("not,it is not armstrong number")
