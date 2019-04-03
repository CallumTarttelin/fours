"""
Fours

Tests functions in the Deck class in app.fours
"""
from assertpy import assert_that
from app import fours


def test_shuffle():
    """
    Checks decks are shuffled and no longer equal
    may fail VERY rarely, but shouldn't in my lifetime
    """
    deck = fours.Deck()
    deck2 = fours.Deck()
    deck.shuffle()
    deck2.shuffle()
    assert_that(deck).is_not_equal_to(deck2)


def test_cards():
    """
    Checks that there are 52 cards in a deck, each with a valid value and suit
    """
    deck = fours.Deck()
    for _ in range(52):
        card = deck.draw()
        assert_that(card.suit).is_in("Hearts", "Clubs", "Diamonds", "Spades")
        assert_that(card.value).is_in(*range(13))


def test_size():
    """
    Checks a deck has 52 cards
    """
    deck = fours.Deck()
    assert_that(deck.cards).is_length(52)


def test_duplicates():
    """
    check a deck of cards has no duplicates, even when converted to a string
    """
    deck = fours.Deck()
    assert_that(len(set(deck.cards))).is_equal_to(len(deck.cards))
    assert_that(len({x.__repr__() for x in deck.cards}))\
        .is_equal_to(len([x.__repr__() for x in deck.cards]))


def test_out():
    """
    Checks that when out of cards it raises the correct exception
    """
    deck = fours.Deck()
    for _ in range(52):
        deck.draw()
    assert_that(deck.draw).raises(fours.OutOfCards).when_called_with()
