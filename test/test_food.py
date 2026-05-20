import pytest
from src.food import calculate_delivery_fee



#region TC019 - TC024
def test_tc019():
    assert calculate_delivery_fee(
        order_amount=100,
        delivery_time="NON_PEAKHOURS",
        membership_status="PREMIUM",
        delivery_distance=19
    ) == 0

def test_tc020():
    assert calculate_delivery_fee(
        order_amount=67,
        delivery_time="NON_PEAKHOURS",
        membership_status="PREMIUM",
        delivery_distance=25
    ) == "Invalid"

def test_tc021():
    assert calculate_delivery_fee(
        order_amount=6767,
        delivery_time="PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=14
    ) == 0

def test_tc022():
    assert calculate_delivery_fee(
        order_amount=167,
        delivery_time="PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=29
    ) == "Invalid"

#endregion
