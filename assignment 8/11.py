# WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.
def armstrongnumber():
    num=int(input("enter the number"))
    temp=num
    count=0
    while(num!=0):

       num=num//10
       count=count+1
    num=temp
    sum=0
    while(num!=0):

      a=num%10
      num=num//10
      sum=sum+(a**count)
    if(sum==temp):

      print("yes,it is a armstrong number")
    else:
     print("not,it is not armstrong number") 
armstrongnumber()        