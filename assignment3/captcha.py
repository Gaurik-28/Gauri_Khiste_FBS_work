import random
userid=input("enter the userid")
password=input("enter the password")
if(userid=="FBS" and password=="FBS123"):
    captcha=random.randint(1000,9999)
    print("captcha:",captcha)
    input=int(input("enter the captcha"))
    if(input==captcha):
        print("login successfully")
    else:
        print("wrong captcha")   
else:
    print("wrong incorrect userid and password")         