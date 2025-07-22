# 9. Write a program to check if entered number is a palindrome or not.
def palindrome():
    num=int(input("enter the three digit number"))
    temp=num
    a=num%10#3
    num=num//10#12
    b=num//10#1
    c=num%10#2
    reverse=(a*100+c*10+b)
    
    if(temp==reverse):
        print("it is palindrome")
    else:
        print("it is not palindrome")    
palindrome()
