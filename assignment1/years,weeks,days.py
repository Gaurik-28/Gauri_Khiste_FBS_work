#Write a program to convert days into years, weeks and days.
days=int(input("enter the no of days:"))
years=days//365
days=days%365
weeks=days//7
days=days%7
print("The no of years",years )
print("The no of weeks",weeks)
print("The no of days",days)
