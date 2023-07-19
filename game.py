import pygame

class Game:
    def __init__(self):
        pygame.init()
        # screen
        self.screen = pygame.display.set_mode((600, 800), 0, 32)
        pygame.display.set_caption("tetris")
        # utilities, clock, game_over
        self.clock = pygame.time.Clock()
        self.game_over = False

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.update()

    def cleanup(self):
        pygame.quit()
