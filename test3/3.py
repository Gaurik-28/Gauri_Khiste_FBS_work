# Write a program to accept basic salary of n emp. (n should be
# accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
# hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.
n=int(input("enter the no  of employ"))
total_salary=0
for i in range(1,n):
   
    basic_salary=float(input("enter the basic salary"))
    if(n<20000):
        da=0.01
        ta=0.12
        hra=0.15
        total=(da*basic_salary+ta*basic_salary+hra*basic_salary)
        print(total)
    else:
        da=0.15
        ta=0.18
        hra=0.20
        total=(da*basic_salary+ta*basic_salary+hra*basic_salary)
        print(total)
    total_salary=total_salary+total  
print(total_salary)      

