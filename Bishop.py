import pygame
from Queen import *


class Bishop(Queen):
    i_am_bishop = True
    
    def __init__(self, position, color, board):
        self.white_bishop_img = pygame.transform.scale(pygame.image.load('Pieces/white_bishop.png'),
                                                     (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.black_bishop_img = pygame.transform.scale(pygame.image.load('Pieces/black_bishop.png'),
                                                     (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.board = board
        self.file = position[0]
        self.rank = position[1]
        self.x_cor = self.board.file_to_x_cor(self.file)
        self.y_cor = self.board.rank_to_y_cor(self.rank)
        self.selected = False
        self.color = color

        if color == 'white':
            self.img = self.white_bishop_img
        elif color == 'black':
            self.img = self.black_bishop_img

    def find_possible_squares(self, own_pieces, opponent_pieces):
        possible_squares = []
        possible_squares = self.add_all_diagonals(possible_squares)
        possible_squares = self.remove_outside_squares(possible_squares)
        possible_squares = self.remove_blocked_diagonals(possible_squares, own_pieces, opponent_pieces)
        possible_squares = self.remove_own_pieces(possible_squares, own_pieces)
        return possible_squares
