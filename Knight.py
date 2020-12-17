import pygame


class Knight:
    i_am_knight = True

    def __init__(self, position, color, board):
        self.white_knight_img = pygame.transform.scale(pygame.image.load('Pieces/white_knight.png'),
                                                       (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.black_knight_img = pygame.transform.scale(pygame.image.load('Pieces/black_knight.png'),
                                                       (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.board = board
        self.color = color
        self.file = position[0]
        self.rank = position[1]
        self.x_cor = self.board.file_to_x_cor(self.file)
        self.y_cor = self.board.rank_to_y_cor(self.rank)
        self.selected = False

        if color == 'white':
            self.img = self.white_knight_img
        elif color == 'black':
            self.img = self.black_knight_img

    def find_possible_squares(self, own_pieces, opponent_pieces):
        possible_squares = []
        possible_squares = self.add_all_possible_squares(possible_squares)
        possible_squares = self.remove_outside_squares(possible_squares)
        possible_squares = self.remove_own_pieces(possible_squares, own_pieces)
        return possible_squares

    def add_all_possible_squares(self, possible_squares):
        possible_squares.append([self.file + 2, self.rank + 1])
        possible_squares.append([self.file + 2, self.rank - 1])
        possible_squares.append([self.file - 2, self.rank + 1])
        possible_squares.append([self.file - 2, self.rank - 1])
        possible_squares.append([self.file + 1, self.rank + 2])
        possible_squares.append([self.file + 1, self.rank - 2])
        possible_squares.append([self.file - 1, self.rank + 2])
        possible_squares.append([self.file - 1, self.rank - 2])
        return possible_squares
        
    @staticmethod
    def remove_outside_squares(possible_squares):
        to_be_removed_squares = []
        for square in possible_squares:
            if square[0] < 0 or square[0] > 7 or square[1] > 7 or square[1] < 0:
                to_be_removed_squares.append(square)
        for square in to_be_removed_squares:
            possible_squares.remove(square)
        return possible_squares

    @staticmethod
    def remove_own_pieces(possible_squares, own_pieces):
        for piece in own_pieces:
            if [piece.file, piece.rank] in possible_squares:
                possible_squares.remove([piece.file, piece.rank])
        return possible_squares
