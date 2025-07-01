
interior_area = float(input("Enter interior wall area (sq.m): "))
interior_rate = float(input("Enter cost per sq.m for interior: "))

exterior_area = float(input("Enter exterior wall area (sq.m): "))
exterior_rate = float(input("Enter cost per sq.m for exterior: "))


interior_cost = interior_area * interior_rate
exterior_cost = exterior_area * exterior_rate
total_cost = interior_cost + exterior_cost


print("Interior wall painting cost is:", interior_cost)
print("Exterior wall painting cost is:", exterior_cost)
print("Total painting cost is:", total_cost)

