# Function to calculate the discount 
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# final price
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price}")
else:
    print(final_price)
