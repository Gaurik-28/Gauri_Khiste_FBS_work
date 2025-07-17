for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if(j==1 or i==j or i==5):
            print(i,end=" ")
        else:
            print(" ",end=" ")    
    print()  
#           1 
#         2 2
#       3   3
#     4     4
#   5 5 5 5 5          





    