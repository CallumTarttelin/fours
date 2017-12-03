import fours
from time import sleep


class Robot(object):
    def __init__(self):
        self.scores = []
        self.highest = None
        self.lowest = None

    def game(self):
        # Plays The Game
        game = fours.Fours()
        while game.deck.cards != []:
            game.draw_card()
            self.clear_cards(game)
            self.move_cards(game)
            self.clear_cards(game)
        self.scores.append(game.final_cards)

    def game_verbose(self):
        # Plays The Game verbosely
        game = fours.Fours()
        while game.deck.cards != []:
            print("New Turn!")
            game.draw_card()
            print(game)
            self.clear_cards(game)
            print(game)
            sleep(0.1)
        print(game.final_cards)

    def play(self, number):
        [self.game() for x in range(number)]

    def move_cards(self, game):
        # TODO
        # Can we clear a space by moving, by moving clear all under it, all under it < and same suit
        # Or Same suit and greater than top card, clears top card
        # Then
        # Clear what clears the most cards
        # Decide by left most one
        for clear in range(len(game.board)):
            if not game.board[clear]:
                if not self.check_free(game, clear):
                    self.most_clear(game, clear)

    def turn(self, game):
        pass

    def check_free(self, game, clear):
        for x in range(len(game.board)):
            if len(game.board[x]) > 2:
                if game.board[x][-1:][0].value < game.board[x][-2:][0].value\
                        and game.board[x][-1:][0].suit == game.board[x][-2:][0].suit:
                    game.move_card(x, clear)
                    self.clear_cards(game)
                elif game.board[x][-1:][0].value > max([thing.value for thing in game.board[x][:-1]])\
                        and not [False for thing in game.board[x] if thing.suit != game.board[x][-1:][0].suit]:
                        game.move_card(x, clear)
                        self.clear_cards(game)
                else:
                    return False

    def most_clear(self, game, clear):
        board = [] + game.board
        cards_left = []
        for x in range(len(board)):
            if len(game.board[x]) >= 2:
                game.move_card(x, clear)
                self.clear_cards(game)
                cards_left.append(game.final_cards)
                game.board = board
        if cards_left != []:
            game.move_card(cards_left.index(min(cards_left)), clear)
            self.clear_cards(game)
        # What makes the most cards cleared?
        # Do I branch, Do I not?
        # Try Each, Count which is most?
        # Is there a nice algorithm?
        # Most till there is the wrong suit?

    def first_one(self, game, clear):
        for x in range(len(game.board)):
            if game.move_card(x, clear):
                self.clear_cards(game)
                break

    def clear_cards(self, game):
        old = 0
        while game.final_cards != old:
            old = game.final_cards
            self.clear_the_cards(game)

    def clear_the_cards(self, game):
        for x in range(len(game.board)):
            while True:
                if game.board[x] != [] and game.clear_card(x):
                    pass
                else:
                    break
        self.move_cards(game)
