import pytest
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
