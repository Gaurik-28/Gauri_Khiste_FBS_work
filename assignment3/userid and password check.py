correct_userid="gaurik"
correct_password="gaurik123"
entered_userid=input("enter the userid")
entered_password=input("enter the password")

if(correct_password==entered_password and correct_userid==entered_userid):
    print("login successfully")
else:
    print("incorrect username and password, please try later")    