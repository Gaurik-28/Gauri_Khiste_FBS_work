# start=int(input("enter the start number"))
# stop=int(input("enter the stop number"))
# for i in range(start,stop):
#     if(i%8==0):
#         continue
#     else:
#         print(i)


start=int(input("enter the start number"))
stop=int(input("enter the stop number"))
for i in range(start,stop):
    if(i%8==0):
        break
    else:
        print(i)
 
