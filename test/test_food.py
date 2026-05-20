import pytest
from src.delivery import calculate_delivery_fee


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