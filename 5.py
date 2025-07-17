for i in range(1,6):
    for j in range(1,7-i):
        print(" ",end=" ")
    x=65
    for j in range(1,i+1):
        print(chr(x),end="   " )
        x=x+1
    print()  