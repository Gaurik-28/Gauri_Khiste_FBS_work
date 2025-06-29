price=float(input("Enter Price :"))
discount_percentage=float(input("Enter discount % :"))
discount=(price*discount_percentage/100)
selling_price=price-discount
print("Cost Price:",price)
print("Discount:",discount)
print("Selling Price:",selling_price)
