"""
   Business Rules: 
   - Orders below $10 incur $3 service fee 
   - Orders above $50 get free delivery 
   - Peak hour delivery adds $2 
   - Premium members always get free delivery 
   - Delivery distance above 20 km is unavailable
"""

def calculate_delivery_fee(order_amount, delivery_time, membership_status, delivery_distance):
    # Free for Premium or large orders
    if membership_status.lower() == "premium":
        return 0

    if order_amount > 50:
        return 0

    delivery_fee = 5

    if order_amount < 10:
        delivery_fee += 3

    # Peak hour 
    if delivery_time.lower() == "peak":
        delivery_fee += 2

    return delivery_fee