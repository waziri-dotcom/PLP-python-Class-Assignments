# Function to calculate discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # apply discount only if 20% or more
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # return original price if discount < 20%


# --- Main program ---

# Ask user for input
price = float(input("Enter the original price: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Final price: ${final_price:.2f}")
