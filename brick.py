import pygame
import settings
from settings import grid, brick_shapes

class Brick:
    grid_size = grid["size"]
    brick_rectangles = []

    def __init__(self, pos, board, shape):
        self.shape = shape
        self.board = board
        self.pos = pos
        self.shape_index = 0
        self.set_brick_rectangles()
        self.number_of_shapes = self.get_number_of_shapes()

    def set_brick_rectangles(self):
        self.brick_rectangles = self.load_brick_rectangles(shape=self.shape, index=self.shape_index)

    def load_brick_rectangles(self, shape, index):
        brick_rectangles = []
        for i, line in enumerate(shape[index]):
            for k, v in enumerate(line):
                if v == 1:
                    brick_rectangles.append((self.pos[0] + k,
                                             self.pos[1] + i))
        return brick_rectangles

    def set_shape_index(self, index):
        self.shape_index = index

    def set_pos(self, pos):
        self.pos = pos

    def get_number_of_shapes(self):
        return len(self.shape)

    def get_next_shape_index(self):
        return (self.shape_index + 1) % self.number_of_shapes

    def rotate(self, board):
        if self.can_rotate(board):
            new_shape_index = self.get_next_shape_index()
            self.set_shape_index(new_shape_index)
            self.set_brick_rectangles()


    def render(self, screen):
        for r in self.brick_rectangles:
            pygame.draw.rect(screen, (100, 100, 100), [self.board.column_offset/2+r[0]*self.grid_size,
                                                       self.board.row_offset/2+r[1]*self.grid_size,
                                                       self.grid_size,
                                                       self.grid_size])

    def move_down(self, board):
        if self.can_move_down(board):
            self.move((self.pos[0], self.pos[1]+1))

    def can_move_right(self, board):
        for r in self.brick_rectangles:
            if r[0] >= board.cols - 1:
                return False
        return True

    def can_move_left(self, board):
        for r in self.brick_rectangles:
            if r[0] == 0:
                return False
        return True

    def can_move_down(self, board):
        for r in self.brick_rectangles:
            if r[1] >= board.rows - 1 or (r[0], r[1]+1) in board.filled_blocks:
                return False
        return True

    def can_rotate(self, board):
        brick_rectangles = self.load_brick_rectangles(shape=self.shape, index=self.get_next_shape_index())
        for r in brick_rectangles:
            if r[0] < 0 or r[0] > board.cols-1 or r[1] >= board.rows-1:
                return False
        return True

    def move_right(self, board):
        if self.can_move_right(board):
            self.move((self.pos[0] + 1, self.pos[1]))

    def move_left(self, board):
        if self.can_move_left(board):
            self.move((self.pos[0] - 1, self.pos[1]))

    def move(self, pos):
        self.set_pos(pos)
        self.set_brick_rectangles()
