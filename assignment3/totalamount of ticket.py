# Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
a1=int(input("enter the age"))
a2=int(input("enter the age"))
a3=int(input("enter the age"))
a4=int(input("enter the age"))
a5=int(input("enter the age"))
amount=100
fair=0
if(a1<12):
    fair+=amount*0.7
elif(a1>59):
    fair+=amount*0.5
else:
    fair+=amount
if(a2<12):
    fair+=amount*0.7
elif(a2>59):
    fair+=amount*0.5
else:
    fair+=amount 
if(a3<12):
    fair+=amount*0.7
elif(a3>59):
    fair+=amount*0.5
else:
    fair+=amount  
if(a4<12):
    fair+=amount*0.7
elif(a4>59):
    fair+=amount*0.5
else:
    fair+=amount 
if(a5<12):
    fair+=amount*0.7
elif(a5>59):
    fair+=amount*0.5
else:
    fair+=amount 
print(fair)               
