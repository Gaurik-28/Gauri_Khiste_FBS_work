p=int(input("enter the principle amount:"))
r=int(input("enter the rate of interest:"))
n=int(input("enter the Number of times interest is compounded per year"))
t=int(input("enter the no of years"))
compound_interest=p*(1+r/n)**(n*t)
print("the compound interest",compound_interest)