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

def compute_bus_fare(
    age,
    day_type,
    hour,
    trip_duration,
    is_public_holiday
):
    return -1