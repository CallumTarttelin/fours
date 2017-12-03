import random


class Fours(object):
    def __init__(self):
        self.board = [[], [], [], []]
        self.deck = Deck()
        self.deck.shuffle()
        self.final_cards = None

    def __repr__(self):
        biggest = max([len(thing) for thing in self.board])
        out = ""
        for x in range(biggest):
            for y in self.board:
                try:
                    out += "%s | " % str(y[x])
                except IndexError:
                    out += "     | "
            out += "\n"
        return out

    def count_game(self):
        self.final_cards = sum([len(thing) for thing in self.board])

    def draw_card(self):
        try:
            for stack in self.board:
                stack.append(self.deck.draw())
            self.count_game()
            return self
        except OutOfCards:
            self.count_game()
            return self.final_cards

    def clear_card1(self, column):
        # TODO make this less bad, and no I don't know why it needs an 8 line indent, but it does
        # TODO Make this less than a 12 line if statement, please
        if self.board[0] != [] \
                and self.board[0][-1:][0].value > self.board[column][-1:][0].value\
                and self.board[0][-1:][0].suit == self.board[column][-1:][0].suit \
                or self.board[1] != [] \
                and self.board[1][-1:][0].value > self.board[column][-1:][0].value\
                and self.board[1][-1:][0].suit == self.board[column][-1:][0].suit \
                or self.board[2] != [] \
                and self.board[2][-1:][0].value > self.board[column][-1:][0].value \
                and self.board[2][-1:][0].suit == self.board[column][-1:][0].suit \
                or self.board[3] != [] \
                and self.board[3][-1:][0].value > self.board[column][-1:][0].value \
                and self.board[3][-1:][0].suit == self.board[column][-1:][0].suit:
                self.count_game()
                self.board[column].pop()
                return self
        else:
            return False

    def clear_card(self, column):
        for thing in self.board:
            if thing != []:
                if thing[-1:][0].value > self.board[column][-1:][0].value \
                        and thing[-1:][0].suit == self.board[column][-1:][0].suit:
                        self.board[column].pop()
                        self.count_game()
                        return self
        return False

    def move_card(self, start, end):
        if self.board[end] == [] and self.board[start] != []:
            self.board[end].append(self.board[start].pop())
            return self
        else:
            return False


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def __repr__(self):
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        if self.value == 8:
            return "%s %s" % (values[self.value], self.suit[:1])
        else:
            return "%s  %s" % (values[self.value], self.suit[:1])

    def __hash__(self):
        return ("%s:%s" % (self.suit, self.value)).__hash__()


class Deck(object):
    def __init__(self):
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        self.cards = []
        for suit in suits:
            self.cards += [Card(suit, value) for value in range(13)]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise OutOfCards()


class OutOfCards(Exception):
    pass
