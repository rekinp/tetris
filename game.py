import random

import pygame
from pygame.locals import *
from settings import screen, grid, brick_shapes, brick_types
from brick import Brick
from board import Board

class Game:
    rows: int
    cols: int
    row_offset: int
    column_offset: int
    def __init__(self):
        pygame.init()
        # screen
        self.screen_size = (screen["width"], screen["height"])
        self.grid_size = grid["size"]
        self.screen = pygame.display.set_mode(self.screen_size, 0, 32)
        pygame.display.set_caption("tetris")
        # utilities, clock, game_over
        self.board = Board(self.screen)
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.pause = False
        self.brick = Brick(pos=(3, 0), board=self.board, shape=brick_shapes[random.choice(brick_types)])
        self.fps = 3

    def run(self):
        while not self.game_over:
            self.handle_events()
            if not self.pause:
                self.update()
                self.render()
                self.clock.tick(self.fps)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pause = not self.pause
                if event.key == pygame.K_SPACE:
                    self.brick.rotate(self.board)
                if event.key == pygame.K_DOWN:
                    self.brick.move_down(self.board)
                if event.key == pygame.K_RIGHT:
                    self.brick.move_right(self.board)
                if event.key == pygame.K_LEFT:
                    self.brick.move_left(self.board)

    def update(self):
        if self.brick.can_move_down(self.board):
            self.brick.move_down(self.board)
        else:
            for b in self.brick.brick_rectangles:
                self.board.add_filled_block(b)
            self.brick = Brick(pos=(3, 0), board=self.board, shape=brick_shapes[random.choice(brick_types)])
        if self.board.extract_filled_lines() is not None:
            self.board.extract_filled_lines().sort()
        for l in self.board.extract_filled_lines():
            self.board.remove_filled_line(l)
            self.board.move_previous_lines_down(l)
        if len([b[1] for b in self.board.filled_blocks if b[1] <= 0]) > 0:
            self.game_over = True

    def render(self):
        self.screen.fill((0, 0, 0))
        self.board.render(self.screen)
        self.brick.render(self.screen)
        pygame.display.update()

    def cleanup(self):
        pygame.quit()
