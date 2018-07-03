from fours import Fours

from tkinter import *
from tkinter import ttk


# c = game.clear_card
# d = game.draw_card
# m = game.move_card
# b = game.board

class Handlers(object):
    def __init__(self):
        # Tk setup
        self.scoreHeight = 280
        self.next = 0  # 0 for unselected, 1 for clear a card, 2 for move first card, 3 for where to move to
        self.toMove = 0  # which column to move if first card selected
        self.root = Tk()
        self.root.title("Fours")
        # Create Variables
        self.board = StringVar()
        self.scores = []
        self.scoreString = StringVar()
        self.deckSize = IntVar()
        self.helpText = StringVar()
        # Configure grid
        mainframe = ttk.Frame(self.root, padding='3 3 12 12', height=1000)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        # Add all labels and buttons
        # Game Board
        ttk.Label(mainframe, textvariable=self.board, font=('Consolas', 14)).grid(column=0, row=0, columnspan=4, rowspan=4, sticky=(N, W))
        # Scores
        ttk.Label(mainframe, text="Scores").grid(column=4, row=0, sticky=(N, E))
        self.scoreLabel = ttk.Label(mainframe, textvariable=self.scoreString)
        self.scoreLabel.grid(column=4, row=1, rowspan=3, pady=(10, self.scoreHeight), sticky=E)
        # DeckSize
        ttk.Label(mainframe, text="Deck").grid(column=4, row=4, sticky=E)
        ttk.Label(mainframe, textvariable=self.deckSize).grid(column=4, row=5, sticky=(S, E))
        # Helper label
        ttk.Label(mainframe, textvariable=self.helpText).grid(column=0, row=6, columnspan=5, sticky=(N, E, W))
        # A B C D buttons
        for x in range(4):
            y = ttk.Button(mainframe, text=["A", "B", "C", "D"][x])
            y.grid(column=x, row=4)
            y.bind('<1>', self.handle_letter)
        # Clear Move Draw New buttons
        ttk.Button(mainframe, text="Clear", command=self.handle_clear).grid(column=0, row=5)
        ttk.Button(mainframe, text="Move", command=self.handle_move).grid(column=1, row=5)
        ttk.Button(mainframe, text="Draw", command=self.handle_draw).grid(column=2, row=5)
        ttk.Button(mainframe, text="New", command=self.handle_new).grid(column=3, row=5)
        # Game setup
        self.fours = Fours()
        self.handle_draw()
        self.helpText.set("")

    def handle_letter(self, event):
        position = 'ABCD'.index(event.widget['text'])
        if self.next == 0:
            self.helpText.set("")
            return
        elif self.next == 1:
            if not self.fours.clear_card(position):
                self.helpText.set("Invalid clear, needs card of greater value and same suit on board")
            self.update()
        elif self.next == 2:
            if self.fours.board[position] == []:
                self.helpText.set("Invalid movement, no card on pile")
                self.next = 0
                return
            self.toMove = position
            self.next = 3
            self.helpText.set("Which column to move {0} to?".format(self.fours.board[position][-1]))
            self.update()
        elif self.next == 3:
            if not self.fours.move_card(self.toMove, position):
                self.helpText.set("Invalid movement, card must go onto empty pile")
            self.update()
            self.next = 0
            self.helpText.set("Card moved from {0} to {1}!".format('ABCD'[self.toMove], 'ABCD'[position]))
        else:
            raise ValueError  # Not in correct range of values

    def handle_clear(self):
        self.next = 1
        self.helpText.set("Clear a card in a column by pressing the button!")

    def handle_move(self):
        self.next = 2
        self.helpText.set("Pick a card to move!")

    def handle_draw(self):
        self.fours.draw_card()
        self.update()
        self.next = 0
        self.helpText.set("Drawn 4 more cards!")

    def handle_new(self):
        if self.fours.deck.cards != []:
            self.popup()
        else:
            self.new_game()

    def new_game(self):
        self.fours.count_game()
        score = self.fours.final_cards + len(self.fours.deck.cards)
        self.scores.append(score)
        self.scoreString.set("\n".join([str(x) for x in self.scores[-17:]]))
        self.scoreHeight -= 15
        self.scoreLabel.grid(pady=(10, self.scoreHeight if self.scoreHeight > 25 else 25))
        self.fours = Fours()
        self.handle_draw()
        self.next = 0
        self.helpText.set("You scored {0}!".format(score))

    def update(self):
        self.board.set(self.fours.__repr__())
        self.deckSize.set(len(self.fours.deck.cards))

    def popup(self):
        def handle(close):
            if close:
                self.new_game()
            win.destroy()
        win = Toplevel()
        win.wm_title("Cards Remain!")
        ttk.Label(win, text="You have {0} cards left,\ndo you really want to start a new game?".format(len(self.fours.deck.cards))).grid(row=0, column=0, columnspan=2, sticky=(N, E, W))
        ttk.Button(win, text="Yes", command=lambda: handle(True)).grid(padx=(0, 10), pady=10, row=1, column=0, sticky=(S, W))
        ttk.Button(win, text="No", command=lambda: handle(False)).grid(padx=(10, 0), pady=10, row=1, column=1, sticky=(S, E))

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    ui = Handlers()
    ui.start()
