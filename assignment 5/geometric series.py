# Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter the number of terms (n): "))

a = 1   
r = 2   
sum_series = a * (r**n - 1) // (r - 1)

print(f"Sum of the geometric series (1 + 2 + 4 + ... up to {n} terms) is: {sum_series}")




