"""
    Compute the price of a bus ride based on multiple rules:
    - Children under 2 ride for free
    - Children under 18 and seniors over 65 pay half fare
    - Adults pay the full fare of $3
    - Peak hours (Mon–Fri, 7–9am, 4–6pm) have a $1.5 surcharge
    - Weekends have a flat fare of $2 (except children under 2)
    - Short trips under 5 minutes during off-peak (Mon–Fri) are free (except weekends)
    - Public holidays have a special $2 surcharge that overrides other rules
"""

def calculate_delivery_fee(order_amount, delivery_time, membership_status, delivery_distance):
    delivery_fee = 10000

    # Distance
    if delivery_distance > 5:
        delivery_fee += (delivery_distance - 5) * 2000

    # Peak time
    if delivery_time.lower() == "peak":
        delivery_fee += 5000

    # Premium
    if membership_status.lower() == "premium":
        delivery_fee *= 0.8  # diskon 20%

    # Free Delivery 
    if order_amount >= 200000:
        delivery_fee = 0

    return delivery_fee