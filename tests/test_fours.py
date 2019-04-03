"""
Fours

Tests functions in the Fours class in app.fours,
this tests most of the other classes by coincidence
"""
from assertpy import assert_that
from app import fours


def test_draw():
    """
    Tests that a non shuffled deck always gives the same board state
    """
    not_shuffled = fours.Deck()
    game = fours.Fours()
    game.deck = not_shuffled
    game.draw_card()
    assert_that(game.board).is_equal_to([
        [fours.Card("Spades", 12)],
        [fours.Card("Spades", 11)],
        [fours.Card("Spades", 10)],
        [fours.Card("Spades", 9)]
    ])


def test_move():
    """
    Checks you can move a card into a free space
    """
    game = fours.Fours()
    game.board = [
        [fours.Card("Spades", 12), fours.Card("Diamonds", 4)],
        [fours.Card("Hearts", 6)],
        [],
        []
    ]
    game.move_card(0, 3)
    assert_that(game.board).is_equal_to([
        [fours.Card("Spades", 12)],
        [fours.Card("Hearts", 6)],
        [],
        [fours.Card("Diamonds", 4)]
    ])


def test_clear():
    """
    Tests you can clear a card if there is a card of same suit but higher value visible
    """
    game = fours.Fours()
    game.board = [
        [fours.Card("Hearts", 12)],
        [fours.Card("Hearts", 6)],
        [],
        []
    ]
    game.clear_card(1)
    assert_that(game.board).is_equal_to([
        [fours.Card("Hearts", 12)],
        [],
        [],
        []
    ])


def test_valid_clear():
    """
    Tests that you cannot clear if the clear wouldn't be valid
    """
    game = fours.Fours()
    game.board = [
        [fours.Card("Hearts", 12)],
        [fours.Card("Spades", 6)],
        [],
        []
    ]
    assert_that(game.clear_card(1)).is_false()
    assert_that(game.board).is_equal_to([
        [fours.Card("Hearts", 12)],
        [fours.Card("Spades", 6)],
        [],
        []
    ])


def test_valid_move():
    """
    Checks you can't move a card to a space with a card already in it
    """
    game = fours.Fours()
    game.board = [
        [fours.Card("Spades", 12), fours.Card("Diamonds", 4)],
        [fours.Card("Hearts", 6)],
        [],
        []
    ]
    assert_that(game.move_card(0, 1)).is_false()
    assert_that(game.board).is_equal_to([
        [fours.Card("Spades", 12), fours.Card("Diamonds", 4)],
        [fours.Card("Hearts", 6)],
        [],
        []
    ])


def test_count_cards():
    """
    Checks that it counts the right number of cards on a finished board
    """
    game = fours.Fours()
    game.board = [[2], [3], [5], [1, 2, 3]]
    game.count_game()
    assert_that(game.final_cards).is_equal_to(6)
