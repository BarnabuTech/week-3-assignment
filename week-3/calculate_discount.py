# This define the calculate_discount function
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The final price after applying the discount (if applicable).
    """
    if discount_percent >= 20:  # Apply discount only if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return the original price if the discount is less than 20%

# Prompting the user for input and calculating the final price
def main():
    try:
        # Get user input for the original price and discount percentage
        original_price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price using the calculate_discount function
        final_price = calculate_discount(original_price, discount_percent)
        
        # Print the result
        if discount_percent >= 20:
            print(f"Final price after applying {discount_percent}% discount: Ksh. {final_price:.2f}")
        else:
            print(f"No discount applied. Original price: ${original_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for price and discount percentage.")

# Run the main function
if __name__ == "__main__":
    main()