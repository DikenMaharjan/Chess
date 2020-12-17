import pygame


class Queen:
    i_am_queen = True

    def __init__(self, position, color, board):
        self.white_queen_img = pygame.transform.scale(pygame.image.load('Pieces/white_queen.png'), 
                                                      (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.black_queen_img = pygame.transform.scale(pygame.image.load('Pieces/black_queen.png'), 
                                                      (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.board = board
        self.color = color
        self.file = position[0]
        self.rank = position[1]
        self.x_cor = self.board.file_to_x_cor(self.file)
        self.y_cor = self.board.rank_to_y_cor(self.rank)
        self.selected = False

        if color == 'white':
            self.img = self.white_queen_img
        elif color == 'black':
            self.img = self.black_queen_img

    def find_possible_squares(self, own_pieces, opponent_pieces):
        possible_squares = []
        possible_squares = self.add_all_files_and_ranks(possible_squares)
        possible_squares = self.add_all_diagonals(possible_squares)
        possible_squares = self.remove_outside_squares(possible_squares)
        possible_squares = self.remove_blocked_files_and_ranks(possible_squares, own_pieces, opponent_pieces)
        possible_squares = self.remove_blocked_diagonals(possible_squares, own_pieces, opponent_pieces)
        possible_squares = self.remove_own_pieces(possible_squares, own_pieces)
        return possible_squares

    def add_all_diagonals(self, possible_squares):
        for i in range(1, 8):
            possible_squares.append([self.file + i, self.rank + i])
            possible_squares.append([self.file - i, self.rank - i])
            possible_squares.append([self.file + i, self.rank - i])
            possible_squares.append([self.file - i, self.rank + i])
        return possible_squares
            
    def add_all_files_and_ranks(self, possible_squares):
        for i in range(1, 8):
            possible_squares.append([self.file, self.rank + i])
            possible_squares.append([self.file - i, self.rank])
            possible_squares.append([self.file, self.rank - i])
            possible_squares.append([self.file + i, self.rank])
        return possible_squares
    
    def remove_blocked_files_and_ranks(self, possible_squares, own_pieces, opponent_pieces):
        all_pieces = own_pieces + opponent_pieces
        to_be_removed_squares = []
        for piece in all_pieces:
            if [piece.file, piece.rank] in possible_squares:
                if piece.file == self.file:
                    if piece.rank < self.rank:
                        for i in range(1, piece.rank + 1):
                            to_be_removed_squares.append([piece.file, piece.rank - i])
                    if piece.rank > self.rank:
                        for i in range(1, 7 - piece.rank + 1):
                            to_be_removed_squares.append([piece.file, piece.rank + i])
                if piece.rank == self.rank:
                    if piece.file < self.file:
                        for i in range(1, piece.file + 1):
                            to_be_removed_squares.append([piece.file - i, piece.rank])
                    if piece.file > self.file:
                        for i in range(1, 7 - piece.file + 1):
                            to_be_removed_squares.append([piece.file + i, piece.rank])
        to_be_removed_squares_final = []
        for x in to_be_removed_squares:
            if x not in to_be_removed_squares_final:
                to_be_removed_squares_final.append(x)
        for square in to_be_removed_squares_final:
            possible_squares.remove(square)
        return possible_squares

    def remove_blocked_diagonals(self, possible_squares, own_pieces, opponent_pieces):
        all_pieces = own_pieces + opponent_pieces
        to_be_removed_squares = []
        for piece in all_pieces:
            if [piece.file, piece.rank] in possible_squares:
                if piece.file > self.file:
                    if piece.rank < self.rank:
                        for i in range(1, piece.rank + 1):
                            if piece.file + i < 8:
                                to_be_removed_squares.append([piece.file + i, piece.rank - i])
                    if piece.rank > self.rank:
                        for i in range(1, 7 - piece.rank + 1):
                            if piece.file + i < 8:
                                to_be_removed_squares.append([piece.file + i, piece.rank + i])
                if piece.file < self.file:
                    if piece.rank < self.rank:
                        for i in range(1, piece.rank + 1):
                            if piece.file - i >= 0:
                                to_be_removed_squares.append([piece.file - i, piece.rank - i])
                    if piece.rank > self.rank:
                        for i in range(1, 7 - piece.rank + 1):
                            if piece.file - i >= 0:
                                to_be_removed_squares.append([piece.file - i, piece.rank + i])
        to_be_removed_squares_final = []
        for x in to_be_removed_squares:
            if x not in to_be_removed_squares_final:
                to_be_removed_squares_final.append(x)
        for square in to_be_removed_squares_final:
            possible_squares.remove(square)
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
