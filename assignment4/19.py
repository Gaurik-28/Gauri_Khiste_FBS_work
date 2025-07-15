# S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = float(input("Enter the value of a: "))
sum_series = 0
for i in range(1, 11): 
    term = (a ** i) / i
    sum_series += term

print("Sum of the series:",sum_series)
