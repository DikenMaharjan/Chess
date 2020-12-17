import pygame


class King:
    i_am_king = True
    moved = False
    
    def __init__(self, position, color, board):
        self.white_king_img = pygame.transform.scale(pygame.image.load('Pieces/white_king.png'),
                                                     (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.black_king_img = pygame.transform.scale(pygame.image.load('Pieces/black_king.png'),
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
            self.img = self.white_king_img
        elif color == 'black':
            self.img = self.black_king_img

    def has_the_king_moved(self):
        if self.initial_file != self.file or self.initial_rank != self.rank:
            self.moved = True

    def find_possible_squares(self, own_pieces, opponent_pieces):
        self.has_the_king_moved()
        possible_squares = []
        possible_squares = self.add_all_possible_squares(possible_squares)
        possible_squares = self.remove_outside_squares(possible_squares)
        possible_squares = self.remove_own_pieces(possible_squares, own_pieces)
        if not self.moved:
            possible_squares = self.add_castling_square(possible_squares, own_pieces, opponent_pieces)
        return possible_squares

    def add_castling_square(self, possible_squares, own_pieces, opponent_pieces):
        if self.is_there_rook_for_castling(own_pieces, direction=1):
            if not self.anything_between_rook_and_king(own_pieces, opponent_pieces, direction=1):
                if not self.obstructed_for_castling(own_pieces, opponent_pieces, direction=1):
                    possible_squares.append([self.file + 2, self.rank])
        if self.is_there_rook_for_castling(own_pieces, direction=-1):
            if not self.anything_between_rook_and_king(own_pieces, opponent_pieces, direction=-1):
                if not self.obstructed_for_castling(own_pieces, opponent_pieces, direction=-1):
                    possible_squares.append([self.file - 2, self.rank])
        return possible_squares

    def obstructed_for_castling(self, own_pieces, opponent_pieces, direction):
        for piece in opponent_pieces:
            if not hasattr(piece, 'i_am_king') or (hasattr(piece, 'i_am_king') and piece.moved):
                squares = piece.find_possible_squares(opponent_pieces, own_pieces)
                for square in squares:
                    for i in range(0, 3):
                        if square[0] == self.file + i * direction and square[1] == self.rank:
                            return True
        return False

    def is_there_rook_for_castling(self, own_pieces, direction):
        possible = False
        for piece in own_pieces:
            if hasattr(piece, 'i_am_rook'):
                if direction == 1:
                    if piece.file > self.file and not piece.moved:
                        possible = True
                if direction == -1:
                    if piece.file < self.file and not piece.moved:
                        possible = True
        return possible

    def anything_between_rook_and_king(self, own_pieces, opponent_pieces, direction):
        all_pieces = own_pieces + opponent_pieces
        for piece in own_pieces:
            if hasattr(piece, 'i_am_rook'):
                if direction == 1 and piece.file > self.file:
                    for i in range(1, 3):
                        for all_piece in all_pieces:
                            if all_piece.file == self.file + i and all_piece.rank == self.rank:
                                return True
                if direction == -1 and piece.file < self.file:
                    for i in range(1, 4):
                        for all_piece in all_pieces:
                            if all_piece.file == self.file - i and all_piece.rank == self.rank:
                                return True
        else:
            return False

    def add_all_possible_squares(self, possible_squares):
        possible_squares.append([self.file + 1, self.rank])
        possible_squares.append([self.file - 1, self.rank])
        possible_squares.append([self.file, self.rank - 1])
        possible_squares.append([self.file, self.rank + 1])
        possible_squares.append([self.file + 1, self.rank + 1])
        possible_squares.append([self.file + 1, self.rank - 1])
        possible_squares.append([self.file - 1, self.rank + 1])
        possible_squares.append([self.file - 1, self.rank - 1])
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
