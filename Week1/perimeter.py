width_1 = float(input("Enter width 1: "))
height_1 = float(input("Enter height 1: "))
width_2 = float(input("Enter width 2: "))
height_2 = float(input("Enter height 2: "))
price_per_metre = float(input("Enter price per metre: "))
op = input("Total fence or Total price: ")

if op == "Total fence":
    print(height_1 + width_1 + width_2 + height_1 + width_1 + width_2)
elif op == "Total price":
    print(price_per_metre * (height_1 + width_1 + width_2 + height_1 + width_1 + width_2) )
else:
    print("Invalid, Please start over and insert Total fence or Total price")
