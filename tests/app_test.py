import unittest
from assertpy import assert_that
from app import fours


class TestFours(unittest.TestCase):
    def test_draw(self):
        not_shuffled = fours.Deck()
        game = fours.Fours()
        game.deck = not_shuffled
        game.draw_card()
        assert_that(game.board).is_equal_to([[fours.Card("Spades", 12)], [fours.Card("Spades", 11)],
                                             [fours.Card("Spades", 10)], [fours.Card("Spades", 9)]])

    def test_move(self):
        game = fours.Fours()
        game.board = [[fours.Card("Spades", 12), fours.Card("Diamonds", 4)],
                      [fours.Card("Hearts", 6)],
                      [],
                      []]
        game.move_card(0, 3)
        assert_that(game.board).is_equal_to([[fours.Card("Spades", 12)],
                                             [fours.Card("Hearts", 6)],
                                             [],
                                             [fours.Card("Diamonds", 4)]])

    def test_clear(self):
        game = fours.Fours()
        game.board = [[fours.Card("Hearts", 12)],
                      [fours.Card("Hearts", 6)],
                      [],
                      []]
        game.clear_card(1)
        self.assertEqual(game.board, [[fours.Card("Hearts", 12)],
                                      [],
                                      [],
                                      []])

    def test_valid_clear(self):
        game = fours.Fours()
        game.board = [[fours.Card("Hearts", 12)],
                      [fours.Card("Spades", 6)],
                      [],
                      []]
        self.assertEqual(game.clear_card(1), False)
        self.assertEqual(game.board, [[fours.Card("Hearts", 12)],
                                      [fours.Card("Spades", 6)],
                                      [],
                                      []])

    def test_valid_move(self):
        game = fours.Fours()
        game.board = [[fours.Card("Spades", 12), fours.Card("Diamonds", 4)],
                      [fours.Card("Hearts", 6)],
                      [],
                      []]
        self.assertEqual(game.move_card(0, 1), False)
        self.assertEqual(game.board, [[fours.Card("Spades", 12), fours.Card("Diamonds", 4)],
                                      [fours.Card("Hearts", 6)],
                                      [],
                                      []])

    def test_count_cards(self):
        game = fours.Fours()
        game.board = [[2], [3], [5], [1, 2, 3]]
        game.count_game()
        self.assertEqual(game.final_cards, 6)


class TestCard(unittest.TestCase):
    def test_suit(self):
        self.assertEqual(fours.Card("Spade", 4).suit, "Spade")

    def test_value(self):
        self.assertEqual(fours.Card("Octocat", 7).value, fours.Card("Octocat", 7).value)

    def test_equals(self):
        self.assertEqual(fours.Card("Diamond", 6), fours.Card("Diamond", 6))
        #assert_that(fours.Card("Diamond", 6)).is_same_as(fours.Card("Diamond", 6))


class TestDeck(unittest.TestCase):
    def test_shuffle(self):
        deck = fours.Deck()
        deck2 = fours.Deck()
        deck.shuffle()
        deck2.shuffle()
        assert_that(deck).is_not_equal_to(deck2)

    def test_cards(self):
        deck = fours.Deck()
        for x in range(52):
            card = deck.draw()
            assert_that(card.suit).is_in("Hearts", "Clubs", "Diamonds", "Spades")
            assert_that(card.value).is_in(*range(13))

    def test_size(self):
        deck = fours.Deck()
        assert_that(deck.cards).is_length(52)

    def test_duplicates(self):
        deck = fours.Deck()
        assert_that(len(set(deck.cards))).is_equal_to(len(deck.cards))

    def test_out(self):
        deck = fours.Deck()
        for x in range(52):
            deck.draw()
        # assert_that(deck.draw).raises(fours.OutOfCards).when_called_with("this")
        self.assertRaises(fours.OutOfCards, deck.draw)
