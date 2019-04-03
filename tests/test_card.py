"""
Fours

Tests functions in the Card class in app.fours
"""
from assertpy import assert_that
from app import fours


def test_constructor():
    """
    Check the card values are set properly
    """
    card = fours.Card("Spade", 4)
    assert_that(card.suit).is_equal_to("Spade")
    assert_that(card.value).is_equal_to(4)


def test_equals():
    """
    Check cards can be checked for equality
    """
    assert_that(fours.Card("Diamond", 6)).is_equal_to(fours.Card("Diamond", 6))
