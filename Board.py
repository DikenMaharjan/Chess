import pygame


class Board:
    BLACK = (0, 0, 0)
    DARK_SQUARE_START = (100, 100, 100)
    DARK_SQUARE_STOP = (105, 43, 50)
    LIGHT_SQUARE_START = (235, 235, 235)
    LIGHT_SQUARE_STOP = (210, 218, 200)
    BORDER_COLOR = (127, 29, 21)
    HIGHLIGHTED_START = (34, 153, 193)
    HIGHLIGHTED_STOP = (45, 230, 178)
    MARKED_COLOR = (34, 34, 43)
    RECENT_START = (43, 34, 12)
    RECENT_STOP = (109, 102, 78)

    highlighted = False
    highlighted_squares = [0, 0]
    recent_moves_show = False
    recent_moves_squares = [[0, 0], [0, 0]]

    turn = 0

    squares = {}
    file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rank = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    def __init__(self, screen, screen_size, board_size):
        self.screen = screen
        self.SCREEN_SIZE = screen_size
        self.BOARD_SIZE = board_size
        self.start_point = (self.SCREEN_SIZE - self.BOARD_SIZE) // 2
        self.SQUARE_SIZE = self.BOARD_SIZE // 8

        for i in range(7, -1, -1):
            for j in range(8):
                square_name = self.file[j] + self.rank[i]
                self.squares[square_name] = (j, i)
                
    # <editor-fold desc="Convert">

    def x_cor_to_file(self, x_cor):
        return (x_cor - self.start_point) // self.SQUARE_SIZE

    def y_cor_to_rank(self, y_cor):
        return (y_cor - self.start_point) // self.SQUARE_SIZE

    def file_to_x_cor(self, file):
        return self.start_point + file * self.SQUARE_SIZE

    def rank_to_y_cor(self, rank):
        return self.start_point + rank * self.SQUARE_SIZE

    # </editor-fold>

    # <editor-fold desc="ColorGradient">
    def draw_color_gradient(self, start_point, length, color1, color2):
        size = length
        for i in range(length // 2):
            r = color1[0] + (i / (length // 2 - 1) * (color2[0] - color1[0]))
            g = color1[1] + (i / (length // 2 - 1) * (color2[1] - color1[1]))
            b = color1[2] + (i / (length // 2 - 1) * (color2[2] - color1[2]))
            x_cor = i + start_point[0]
            y_cor = i + start_point[1]
            square = (x_cor, y_cor, size, size)
            pygame.draw.rect(self.screen, (r, g, b), square, 1)
            size -= 2
    # </editor-fold>
            
    def draw_board(self):
        color = 1
        for square in self.squares.values():
            x_cor = self.file_to_x_cor(square[0])
            y_cor = self.rank_to_y_cor(square[1])
            if color % 2 == 0:
                self.draw_color_gradient((x_cor, y_cor), self.SQUARE_SIZE,
                                         self.LIGHT_SQUARE_START, self.LIGHT_SQUARE_START)
            else:
                self.draw_color_gradient((x_cor, y_cor), self.SQUARE_SIZE,
                                         self.DARK_SQUARE_START, self.DARK_SQUARE_START)

            if square[0] != 7:
                color += 1
    
    def is_it_white_turn(self):
        if self.turn % 2 == 0:
            return True
        else:
            return False

    def highlight_square(self):
        if self.highlighted:
            x_cor = self.file_to_x_cor(self.highlighted_squares[0])
            y_cor = self.rank_to_y_cor(self.highlighted_squares[1])
            self.draw_color_gradient((x_cor, y_cor), self.SQUARE_SIZE, self.HIGHLIGHTED_START, self.HIGHLIGHTED_STOP)

    def change_highlighted_square(self, mouse_position):
        self.highlighted_squares[0] = self.x_cor_to_file(mouse_position[0])
        self.highlighted_squares[1] = self.y_cor_to_rank(mouse_position[1])

    def draw_markers(self, file, rank):
        x_cor = self.file_to_x_cor(file)
        y_cor = self.rank_to_y_cor(rank)
        centre = (x_cor + self.SQUARE_SIZE // 2, y_cor + self.SQUARE_SIZE // 2)
        pygame.draw.circle(self.screen, self.MARKED_COLOR, centre, 5)

    def show_recent_moves(self):
        if self.recent_moves_show:
            x_cor = self.file_to_x_cor(self.recent_moves_squares[0][0])
            y_cor = self.rank_to_y_cor(self.recent_moves_squares[0][1])
            self.draw_color_gradient((x_cor, y_cor), self.SQUARE_SIZE, self.RECENT_START, self.RECENT_STOP)
            x_cor = self.file_to_x_cor(self.recent_moves_squares[1][0])
            y_cor = self.rank_to_y_cor(self.recent_moves_squares[1][1])
            self.draw_color_gradient((x_cor, y_cor), self.SQUARE_SIZE, self.RECENT_START, self.RECENT_STOP)
