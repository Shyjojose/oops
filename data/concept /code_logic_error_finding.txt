def apply_discounts(cart_total, discount_code=None):
    """
    Applies a 10% discount if the total is over $100.
    If a special code 'SAVE20' is used, it adds an extra $20 off.
    """
    
    # Logic 1: Check for bulk discount
    if cart_total > 100:
        cart_total = cart_total * 0.9
        
    # Logic 2: Apply special coupon
    if discount_code == "SAVE20":
        cart_total = cart_total - 20
        
    return cart_total

# Test Case: A user spends $110 and uses the 'SAVE20' code.
# Expected result: $110 - 10% ($11) - $20 = $79
print(f"Final Total: ${apply_discounts(110, 'SAVE20')}")

Spot on! You nailed both the boundary and the safety issues.
Here is why those two logic errors are classic "AI traps":
1.The "Off-By-One" Boundary: By using > 100 instead of >= 100,
 a customer spending exactly $100 gets zero discount. 
In a real project, this leads to angry support tickets.
2.The Negative Balance: If someone buys a $5 item 
and uses a $20 coupon, the store technically "owes" them $15. 
Without a max(0, ...) check, your database would record a negative 
transaction, which can crash accounting software.
