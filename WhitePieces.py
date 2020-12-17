from King import *
from Bishop import *
from Knight import *
from Rook import *
from Queen import *
from Pawn import *


class WhitePieces:
    own_pieces = []
    
    def __init__(self, board):
        self.board = board
        self.own_pieces.append(King(self.board.squares['e1'], 'white', self.board))
        self.own_pieces.append(Queen(self.board.squares['d1'], 'white', self.board))
        self.own_pieces.append(Rook(self.board.squares['h1'], 'white', self.board))
        self.own_pieces.append(Rook(self.board.squares['a1'], 'white', self.board))
        self.own_pieces.append(Knight(self.board.squares['g1'], 'white', self.board))
        self.own_pieces.append(Knight(self.board.squares['b1'], 'white', self.board))
        self.own_pieces.append(Bishop(self.board.squares['c1'], 'white', self.board))
        self.own_pieces.append(Bishop(self.board.squares['f1'], 'white', self.board))
        for i in range(8):
            self.own_pieces.append(Pawn(self.board.squares[self.board.file[i] + '2'], 'white', self.board))
