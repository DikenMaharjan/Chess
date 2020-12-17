from King import *
from Bishop import *
from Rook import *
from Queen import *
from Knight import *
from Pawn import *


class BlackPieces:
    own_pieces = []

    def __init__(self, board):
        self.board = board
        self.own_pieces.append(King(self.board.squares['e8'], 'black', self.board))
        self.own_pieces.append(Queen(self.board.squares['d8'], 'black', self.board))
        self.own_pieces.append(Rook(self.board.squares['h8'], 'black', self.board))
        self.own_pieces.append(Rook(self.board.squares['a8'], 'black', self.board))
        self.own_pieces.append(Knight(self.board.squares['g8'], 'black', self.board))
        self.own_pieces.append(Knight(self.board.squares['b8'], 'black', self.board))
        self.own_pieces.append(Bishop(self.board.squares['c8'], 'black', self.board))
        self.own_pieces.append(Bishop(self.board.squares['f8'], 'black', self.board))
        for i in range(8):
            self.own_pieces.append(Pawn(self.board.squares[self.board.file[i] + '7'], 'black', self.board))
