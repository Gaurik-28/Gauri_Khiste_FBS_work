# 1! + 2! + 3! + 4! + .....n!
n = int(input("Enter the value of n: "))
fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i  # calculate factorial of i
    total += fact  

print(f"Sum of the series 1! + 2! + ... + {n}! is: {total}")
