# WAP to print sum of series upto n.
n = int(input("Enter the value of n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of the series 1 + 2 + ... + {n} is: {total}")
