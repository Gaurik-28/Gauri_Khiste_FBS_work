# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
# Input from user
num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost per ticket: "))

total_amount = 0


for i in range(1, num_passengers + 1):
    age = int(input("Enter age of passenger "))
    
    if age < 12:
        cost = ticket_cost * 0.7  
    elif age > 59:
        cost = ticket_cost * 0.5  
    else:
        cost = ticket_cost  

    total_amount += cost


print("Total ticket amount for all passengers:",total_amount)
