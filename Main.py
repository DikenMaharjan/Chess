from Board import *
from WhitePieces import *
from BlackPieces import *
from Piece import *

SCREEN_SIZE = 560
BOARD_SIZE = 400

# <editor-fold desc="Screen">
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("CHESS")
clock = pygame.time.Clock()
# </editor-fold>
board = Board(screen, SCREEN_SIZE, BOARD_SIZE)
white = WhitePieces(board)
black = BlackPieces(board)
piece = Pieces(white, black, screen, board)
running = True

while running:
    screen.fill(board.BLACK)
    mouse_position = pygame.mouse.get_pos()
    if board.is_it_white_turn():
        turn = 'white'
        player = white
        opponent = black
    else:
        turn = 'black'
        player = black
        opponent = white
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not piece.is_anything_selected():
                if piece.can_be_selected(mouse_position, turn):
                    piece.select_the_piece(mouse_position)
                    piece.find_possible_squares(player.own_pieces, opponent.own_pieces)
                    piece.find_squares_with_no_check(player.own_pieces, opponent.own_pieces)
                    board.highlighted = True
                    board.change_highlighted_square(mouse_position)
                elif not piece.can_be_selected(mouse_position, 'white'):
                    board.highlighted = False
                    piece.dis_select()
                    piece.possible_squares.clear()
            elif piece.is_anything_selected():
                if piece.can_be_moved(mouse_position):
                    board.recent_moves_squares[0] = piece.selected_piece_square()
                    piece.move_piece(mouse_position)
                    board.recent_moves_squares[1] = [board.x_cor_to_file(mouse_position[0]), 
                                                     board.y_cor_to_rank(mouse_position[1])]
                    opponent.own_pieces = piece.captured_list(mouse_position, player.own_pieces, opponent.own_pieces)
                    board.turn += 1
                    board.recent_moves_show = True
                board.highlighted = False
                piece.dis_select()
                piece.possible_squares.clear()
    board.show_recent_moves()
    board.draw_board()
    board.show_recent_moves()
    board.highlight_square()
    piece.show_pieces()
    for square in piece.possible_squares:
        board.draw_markers(int(square[0]), int(square[1]))
    pygame.display.update()
    clock.tick(60)
