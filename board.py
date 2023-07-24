import pygame
from settings import grid

class Board:
    screen_size: tuple
    block_size: int
    cols: int
    rows: int
    column_offset: float
    row_offset: float
    filled_blocks = []

    def __init__(self, screen):
        self.grid_size = grid["size"]
        self.screen_size = (screen.get_size())
        self.determine_grid_size()

    def determine_grid_size(self):
        self.cols = int(self.screen_size[0] // self.grid_size)
        self.column_offset = int(self.screen_size[0] - self.cols * self.grid_size)

        self.rows = int(self.screen_size[1] // self.grid_size)
        self.row_offset = int(self.screen_size[1] - self.rows * self.grid_size)

    def add_filled_block(self, pos):
        self.filled_blocks.append(pos)

    def remove_filled_line(self, line):
        self.filled_blocks = [b for b in self.filled_blocks if b[1] != line]

    def move_previous_lines_down(self, line):
        self.filled_blocks = [(b[0], b[1]+1) if b[1] < line else b for b in self.filled_blocks]

    def extract_filled_lines(self):
        filled_lines = []
        for i in range(self.rows):
            row_full = True
            for j in range(self.cols):
                if (j, i) not in self.filled_blocks:
                    row_full = False
            if row_full:
                filled_lines.append(i)
        return filled_lines

    def render(self, screen):
        for i in range(self.cols):
            for j in range(self.rows):
                if (i, j) in self.filled_blocks:
                    fill = 0
                    color = (0, 255, 0)
                else:
                    fill = 1
                    color = (100, 100, 100)
                pygame.draw.rect(screen, color, [self.column_offset/2 + i * self.grid_size,
                                                                self.row_offset/2 + j * self.grid_size,
                                                                self.grid_size,
                                                                self.grid_size], fill)
