import pygame


class Pawn:
    i_am_pawn = True

    def __init__(self, position, color, board):
        self.white_pawn_img = pygame.transform.scale(pygame.image.load('Pieces/white_pawn.png'),
                                                     (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.black_pawn_img = pygame.transform.scale(pygame.image.load('Pieces/black_pawn.png'),
                                                     (board.SQUARE_SIZE, board.SQUARE_SIZE))
        self.board = board
        self.color = color
        self.file = position[0]
        self.rank = position[1]
        self.start_rank = self.rank
        self.x_cor = self.board.file_to_x_cor(self.file)
        self.y_cor = self.board.rank_to_y_cor(self.rank)
        self.selected = False

        if color == 'white':
            self.img = self.white_pawn_img
            self.direction = 1
        elif color == 'black':
            self.img = self.black_pawn_img
            self.direction = -1

    def find_possible_squares(self, own_pieces, opponent_pieces):
        possible_squares = []
        square = [self.file, self.rank - self.direction]
        if not Pawn.is_the_square_occupied(square, own_pieces, opponent_pieces):
            possible_squares.append(square)
        if self.is_in_starting_position() and not self.is_the_square_occupied(square, own_pieces, opponent_pieces):
            square = [self.file, self.rank - 2 * self.direction]
            if not self.is_the_square_occupied(square, own_pieces, opponent_pieces):
                possible_squares.append(square)
        square = [self.file + 1, self.rank - self.direction]
        if self.is_the_square_occupied(square, [], opponent_pieces):
            possible_squares.append(square)
        square = [self.file - 1, self.rank - self.direction]
        if self.is_the_square_occupied(square, [], opponent_pieces):
            possible_squares.append(square)
        return possible_squares

    @staticmethod
    def is_the_square_occupied(square, own_pieces, opponent_pieces):
        all_pieces = own_pieces + opponent_pieces
        for piece in all_pieces:
            if [piece.file, piece.rank] == square:
                return True
        else:
            return False

    def is_in_starting_position(self):
        if self.rank == self.start_rank:
            return True
        else:
            return False
