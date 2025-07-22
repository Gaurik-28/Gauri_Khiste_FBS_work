n=int(input("enter the number"))
fact=1
for i in range(1,n):
    fact=(i/fact*i)+fact
print(fact)


