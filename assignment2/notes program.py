#program to find minmum number of notes for the given amount
amount=int(input("enter the given amount:"))
#500
n500=amount//500
r_amount=amount%500
#200
n200=r_amount//200
#r_amount%=200
r_amount=r_amount%200
#100
n100=r_amount//100
r_amount=r_amount%100
#50
n50=r_amount//50
r_amount=r_amount%50
#20
n20=r_amount//20
r_amount=r_amount%20
#10
n10=r_amount//10
r_amount=r_amount%10
print(amount)
print(n500)
print(n200)
print(n100)
print(n50)
print(n20)
print(n10)


