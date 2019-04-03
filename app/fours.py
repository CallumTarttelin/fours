"""
The fours game itself
contains all classes to create a game of fours and Fours object exposes the functions to play it
"""
from random import shuffle


class Fours:
    """
    The game itself, creates the game and any way to interface with it
    """

    def __init__(self):
        self.board = [[], [], [], []]
        self.deck = Deck()
        self.deck.shuffle()
        self.final_cards = None

    def __repr__(self):
        biggest = max([len(column) for column in self.board])
        out = ""
        for i in range(biggest):
            out += "| "
            for column in self.board:
                try:
                    out += "{} | ".format(str(column[i]))
                except IndexError:
                    out += "     | "
            out += "\n"
        return out

    def count_game(self):
        """
        Count all the cards on the board and set final cards
        """
        self.final_cards = sum([len(column) for column in self.board])

    def draw_card(self):
        """
        Draw 4 cards from the deck and add one to each column
        :return: self (Fours) if valid otherwise False
        """
        try:
            for stack in self.board:
                stack.append(self.deck.draw())
            self.count_game()
            return self
        except OutOfCards:
            self.count_game()
            return self.final_cards

    def clear_card(self, column_index):
        """
        :param column_index: The index of the column to clear a card from
        :return: self (Fours) if valid otherwise False
        """

        def column_can_clear(column):
            return column != [] \
                and column[-1:][0].value > self.board[column_index][-1:][0].value \
                and column[-1:][0].suit == self.board[column_index][-1:][0].suit

        for col in self.board:
            if column_can_clear(col):
                self.board[column_index].pop()
                self.count_game()
                return self
        return False

    def move_card(self, start, end):
        """
        :param start: The cards starting column
        :param end: The cards ending column
        :return: self if valid, else False
        """
        if self.board[end] == [] and self.board[start] != []:
            self.board[end].append(self.board[start].pop())
            return self
        return False


class Card:
    """
    The cards in the deck, have a suit and value
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __repr__(self):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        pics = {
            "Spades": u"♠",
            "Hearts": u"♥",
            "Diamonds": u"♦",
            "Clubs": u"♣"
        }

        if self.value == 8:
            return "{} {}".format(values[self.value], pics[self.suit])
        return "{}  {}".format(values[self.value], pics[self.suit])

    def __hash__(self):
        return ("{}:{}".format(self.suit, self.value)).__hash__()


class Deck:
    """
    The deck of cards in the card game, contains 52 cards
    """
    def __init__(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        self.cards = []
        for suit in suits:
            self.cards += [Card(suit, value) for value in range(13)]

    def shuffle(self):
        """
        randomise the order of cards in the deck
        """
        shuffle(self.cards)

    def draw(self):
        """
        :return: a card from the deck if card is present
        Throws OutOfCards Exception if the deck is empty
        """
        try:
            return self.cards.pop()
        except IndexError:
            raise OutOfCards()


class OutOfCards(Exception):
    """
    An exception to notify user when deck is out of cards
    """
