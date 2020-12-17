import pygame
from Queen import *


class Rook(Queen):
    i_am_rook = True
    moved = False

    def __init__(self, position, color, board):
        self.white_rook_img = pygame.transform.scale(pygame.image.load('Pieces/white_rook.png'),
                                                     (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.black_rook_img = pygame.transform.scale(pygame.image.load('Pieces/black_rook.png'),
                                                     (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.board = board
        self.initial_file = position[0]
        self.initial_rank = position[1]
        self.file = position[0]
        self.rank = position[1]
        self.x_cor = self.board.file_to_x_cor(self.file)
        self.y_cor = self.board.rank_to_y_cor(self.rank)
        self.selected = False
        self.color = color

        if color == 'white':
            self.img = self.white_rook_img
        elif color == 'black':
            self.img = self.black_rook_img

    def find_possible_squares(self, own_pieces, opponent_pieces):
        self.has_the_rook_moved()
        possible_squares = []
        possible_squares = self.add_all_files_and_ranks(possible_squares)
        possible_squares = self.remove_outside_squares(possible_squares)
        possible_squares = self.remove_blocked_files_and_ranks(possible_squares, own_pieces, opponent_pieces)
        possible_squares = self.remove_own_pieces(possible_squares, own_pieces)
        return possible_squares

    def has_the_rook_moved(self):
        if self.initial_file != self.file or self.initial_rank != self.rank:
            self.moved = True
