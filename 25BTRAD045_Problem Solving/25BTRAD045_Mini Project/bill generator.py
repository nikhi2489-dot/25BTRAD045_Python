print("===== BILL GENERATOR =====")

item1 = input("Enter first item: ")
price1 = float(input("Enter price: "))

item2 = input("Enter second item: ")
price2 = float(input("Enter price: "))

item3 = input("Enter third item: ")
price3 = float(input("Enter price: "))

total = price1 + price2 + price3

print("\n===== BILL =====")
print(f"{item1} : ₹{price1:.2f}")
print(f"{item2} : ₹{price2:.2f}")
print(f"{item3} : ₹{price3:.2f}")
print("------------------")

print(f"Total Bill: ₹{total:.2f}")
print("==================")
