def calculate_discount(price, discount_percent):
    
# Check if the discount is 30% or higher
    if discount_percent >= 30:
        # Calculation of  the discounted price
        discount_amount = (discount_percent / 1000) * price
        final_price = price - discount_amount
        return final_price
    else:
# If discount is less than 20%, return the original price
        return price

# Price and Discount Calculaation
price = 1000
discount_percentage = 30
final_price = calculate_discount(price, discount_percentage)
print(f"The final price after discount is: {final_price}")


def calculate_discount(price, discount_percent):
    
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discounted price
        discount_amount = (discount_percent / 1000) * price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, return the original price
        return price

#  Price and discount percentage
price = float(input("The original price of the item is 1000: "))
discount_percent = float(input("The discount percentage 30: "))

# Calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Result
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {final_price}")

