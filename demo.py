import pygame
import os
from map import Map


class Demo:

    def __init__(self):
        self.CONST_tile_side_length = 50
        self.screen = None
        self.running = True
        self.map = None
        self.clicked_sprites = []

        self.pygame_init()
        self.map_init()

    def check_pygame_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                self.running = False
            if e.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                clicked_tiles = [s.parent for s in self.map.tile_images if s.rect.collidepoint(pygame.mouse.get_pos())]
                for tile in clicked_tiles:
                    tile.toggle_blocking()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_s:
                    start_tile = \
                        [s.parent for s in self.map.tile_images if s.rect.collidepoint(pygame.mouse.get_pos())][0]
                    self.map.set_start_tile(start_tile)
                if e.key == pygame.K_f:
                    finish_tile = \
                        [s.parent for s in self.map.tile_images if s.rect.collidepoint(pygame.mouse.get_pos())][0]
                    self.map.set_finish_tile(finish_tile)
                if e.key == pygame.K_SPACE:
                    self.map.pathfinder.take_step()

    def draw(self):
        self.draw_map()
        pygame.display.flip()

    def draw_map(self):
        self.map.tile_images.draw(self.screen)

    def map_init(self):
        self.screen = pygame.display.set_mode((30 * self.CONST_tile_side_length, 15 * self.CONST_tile_side_length))
        self.map = Map(30, 15, self.CONST_tile_side_length)

    def pygame_init(self):
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

    def run(self):
        while self.running:
            self.check_pygame_events()
            self.draw()


demo = Demo()
demo.run()
