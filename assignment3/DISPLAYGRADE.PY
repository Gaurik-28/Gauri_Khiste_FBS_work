math=int(input("enter the marks of math"))
history=int(input("enter the marks of history"))
marathi=int(input("enter the marks of marathi"))
english=int(input("enter the marks of english"))
science=int(input("enter the marks of science"))
percentage=((math+history+marathi+english+science)/500)*100
if(percentage>=90):
    print("first class with distintion")
elif(percentage>=80):
    print("first class")    
elif(percentage>=60):
    print("second class") 
elif(percentage>=40):
    print("higher secondary class")   
else:
    print("failed")   



