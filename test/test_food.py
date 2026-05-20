import pytest
from src.food import calculate_delivery_fee


def Test_TC_007():
    # Test case for orders below $10 with peak hour delivery
    assert calculate_delivery_fee(1, "peak", "premium", 10) == 4

def Test_TC_008():
    # Test case for orders below $10 with peak hour delivery and long distance
    assert calculate_delivery_fee(1, "peak", "premium", 25) == "Invalid"

def Test_TC_009():
    # Test case for orders at $10 with non-peak hours, non-premium membership, and distance 20
    assert calculate_delivery_fee(10, "non-peak", "non-premium", 20) == 10

def Test_TC_010():
    # Test case for orders at $13 with non-peak hours, non-premium membership, and distance 25
    assert calculate_delivery_fee(13, "non-peak", "non-premium", 25) == "Invalid"

def Test_TC_011():
    # Test case for orders at $16 with non-peak hours, premium membership, and distance 12
    assert calculate_delivery_fee(16, "non-peak", "premium", 12) == 16

def Test_TC_012():
    # Test case for orders at $28 with non-peak hours, premium membership, and distance 40
    assert calculate_delivery_fee(28, "non-peak", "premium", 40) == "Invalid"
from src.food import calculate_delivery_fee

# Region TC001 - TC006
def test_tc001_non_peak_non_premium():
    assert calculate_delivery_fee(
        order_amount=9,
        delivery_time="NON_PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=20
    ) == 12


def test_tc002_non_peak_non_premium_invalid_distance():
    assert calculate_delivery_fee(
        order_amount=9,
        delivery_time="NON_PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=25
    ) == "Invalid"


def test_tc003_non_peak_premium():
    assert calculate_delivery_fee(
        order_amount=7,
        delivery_time="NON_PEAK_HOURS",
        membership_status="PREMIUM",
        delivery_distance=20
    ) == 10


def test_tc004_non_peak_premium_invalid_distance():
    assert calculate_delivery_fee(
        order_amount=7,
        delivery_time="NON_PEAK_HOURS",
        membership_status="PREMIUM",
        delivery_distance=25
    ) == "Invalid"


def test_tc005_peak_non_premium():
    assert calculate_delivery_fee(
        order_amount=4,
        delivery_time="PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=15
    ) == 9


def test_tc006_peak_non_premium_invalid_distance():
    assert calculate_delivery_fee(
        order_amount=4,
        delivery_time="PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=25
    ) == "Invalid"

#region TC013 - TC018
def test_tc013():
    assert calculate_delivery_fee(
        order_amount=39,
        delivery_time="PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=17
    ) == 41

def test_tc014():
    assert calculate_delivery_fee(
        order_amount=45,
        delivery_time="PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=25
    ) == "Invalid"

def test_tc015():
    assert calculate_delivery_fee(
        order_amount=47,
        delivery_time="PEAK_HOURS",
        membership_status="PREMIUM",
        delivery_distance=5
    ) == 47

def test_tc016():
    assert calculate_delivery_fee(
        order_amount=50,
        delivery_time="PEAK_HOURS",
        membership_status="PREMIUM",
        delivery_distance=25
    ) == "Invalid"

def test_tc017():
    assert calculate_delivery_fee(
        order_amount=58,
        delivery_time="NON_PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=10
    ) == 58

def test_tc018():
    assert calculate_delivery_fee(
        order_amount=62,
        delivery_time="NON_PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=30
    ) == "Invalid"

#region TC019 - TC024
def test_tc019():
    assert calculate_delivery_fee(
        order_amount=100,
        delivery_time="NON_PEAKHOURS",
        membership_status="PREMIUM",
        delivery_distance=19
    ) == 100

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
    ) == 6769

def test_tc022():
    assert calculate_delivery_fee(
        order_amount=167,
        delivery_time="PEAK_HOURS",
        membership_status="NON_PREMIUM",
        delivery_distance=29
    ) == "Invalid"

def test_tc023():
    assert calculate_delivery_fee(
        order_amount=267,
        delivery_time="PEAK_HOURS",
        membership_status="PREMIUM",
        delivery_distance=5
    ) == 267

def test_tc024():
    assert calculate_delivery_fee(
        order_amount=121,
        delivery_time="PEAK_HOURS",
        membership_status="PREMIUM",
        delivery_distance=22
    ) == "Invalid"

#endregion
