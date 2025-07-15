# Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate.
# Predefined valid credentials
correct_userid = "admin"
correct_password = "1234"


for attempt in range(1, 4):
    
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    
    if userid == correct_userid and password == correct_password:
        print("Login successful!")
        break
    else:
        print(f"Incorrect credentials. Attempt {attempt} of 3.")
        if attempt == 3:
            print("Too many failed attempts. Program terminated.")
