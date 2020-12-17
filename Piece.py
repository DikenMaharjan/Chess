class Pieces:
    all_pieces = []
    possible_squares = []
    
    def __init__(self, white, black, screen, board):
        self.white = white
        self.black = black
        for piece in white.own_pieces:
            self.all_pieces.append(piece)
        for piece in black.own_pieces:
            self.all_pieces.append(piece)
        self.screen = screen
        self.board = board

    @staticmethod
    def is_the_king_in_check(own_pieces, opponent_pieces):
        for piece in own_pieces:
            if hasattr(piece, 'i_am_king'):
                for opponent_piece in opponent_pieces:
                    possible_moves = opponent_piece.find_possible_squares(opponent_pieces, own_pieces)
                    for move in possible_moves:
                        if move == [piece.file, piece.rank]:
                            return True
        return False

    def can_be_moved(self, mouse_position):
        file = self.board.x_cor_to_file(mouse_position[0])
        rank = self.board.y_cor_to_rank(mouse_position[1])
        for square in self.possible_squares:
            if file == square[0] and rank == square[1]:
                return True
        return False

    def captured_list(self, mouse_position, own_pieces, opponent_pieces):
        file = self.board.x_cor_to_file(mouse_position[0])
        rank = self.board.y_cor_to_rank(mouse_position[1])
        for piece in opponent_pieces:
            if [piece.file, piece.rank] == [file, rank]:
                opponent_pieces.remove(piece)
        self.all_pieces = own_pieces + opponent_pieces
        return opponent_pieces

    @staticmethod
    def assumed_captured_list(file, rank, opponent_pieces):
        temp_list = []
        for piece in opponent_pieces:
            temp_list.append(piece)
        for piece in temp_list:
            if [piece.file, piece.rank] == [file, rank]:
                temp_list.remove(piece)
        return temp_list

    def move_piece(self, mouse_position):
        for piece in self.all_pieces:
            if piece.selected:
                initial_file = piece.file
                piece.file = self.board.x_cor_to_file(mouse_position[0])
                piece.rank = self.board.y_cor_to_rank(mouse_position[1])
                piece.x_cor = self.board.file_to_x_cor(piece.file)
                piece.y_cor = self.board.rank_to_y_cor(piece.rank)
                if hasattr(piece, 'i_am_king'):
                    if piece.file == initial_file + 2:
                        for required_rook in self.all_pieces:
                            if hasattr(required_rook, 'i_am_rook') and piece.color == required_rook.color:
                                if required_rook.file > piece.file:
                                    required_rook.file -= 2
                                    required_rook.x_cor = self.board.file_to_x_cor(required_rook.file)
                    if piece.file == initial_file - 2:
                        for required_rook in self.all_pieces:
                            if hasattr(required_rook, 'i_am_rook') and piece.color == required_rook.color:
                                if required_rook.file < piece.file:
                                    required_rook.file += 3
                                    required_rook.x_cor = self.board.file_to_x_cor(required_rook.file)

    def find_squares_with_no_check(self, own_pieces, opponent_pieces):
        required_squares = []
        for piece in own_pieces:
            if piece.selected:
                for square in self.possible_squares:
                    temp_file = piece.file
                    temp_rank = piece.rank
                    piece.file = square[0]
                    piece.rank = square[1]
                    temp_opponent_pieces = self.assumed_captured_list(square[0], square[1], opponent_pieces)
                    if not self.is_the_king_in_check(own_pieces, temp_opponent_pieces):
                        required_squares.append(square)
                    piece.file = temp_file
                    piece.rank = temp_rank
        self.possible_squares = required_squares

    def find_possible_squares(self, player, opponent):
        for piece in self.all_pieces:
            if piece.selected:
                self.possible_squares = piece.find_possible_squares(player, opponent)

    def dis_select(self):
        for piece in self.all_pieces:
            piece.selected = False
    
    def show_pieces(self):
        for piece in self.all_pieces:
            self.screen.blit(piece.img, (piece.x_cor, piece.y_cor))

    def is_anything_selected(self):
        for piece in self.all_pieces:
            if piece.selected:
                return True
        return False
    
    def can_be_selected(self, mouse_position, color):
        file = self.board.x_cor_to_file(mouse_position[0])
        rank = self.board.y_cor_to_rank(mouse_position[1])
        if color == 'white':
            for piece in self.white.own_pieces:
                if piece.file == file and piece.rank == rank:
                    return True
        else:
            for piece in self.black.own_pieces:
                if piece.file == file and piece.rank == rank:
                    return True
        return False
    
    def selected_piece_square(self):
        for piece in self.all_pieces:
            if piece.selected:
                return [piece.file, piece.rank]
        
    def select_the_piece(self, mouse_position):
        file = self.board.x_cor_to_file(mouse_position[0])
        rank = self.board.y_cor_to_rank(mouse_position[1])
        for piece in self.all_pieces:
            if piece.file == file and piece.rank == rank:
                piece.selected = True
                break
