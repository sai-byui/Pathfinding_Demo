import pygame
import math


class Tile:

    def __init__(self, x_pos, y_pos, side_length):
        self.sf_font = pygame.font.SysFont("Arial", 25)
        self.cost_font = pygame.font.SysFont("Arial", 12)
        self.f_cost = None
        self.g_cost = None
        self.h_cost = None
        self.visited = False
        self.open = False
        self.closed = False
        self.path_to_me = []
        self.is_start = False
        self.is_finish = False
        self.is_blocking = False
        self.side_length = side_length
        self.connections = []
        self.sprite = TileSprite(self)
        self.sprite.image = pygame.Surface([side_length, side_length])
        self.sprite.rect = pygame.Rect(x_pos, y_pos, side_length, side_length)
        self.sprite.image.fill(0xff0000)
        pygame.draw.rect(self.sprite.image, 0xffffff, pygame.Rect(1, 1, side_length - 2, side_length - 2))
        self.bgcolor = 0xffffff

    def update_bg(self, color):
        self.bgcolor = color
        self.set_g_cost(self.g_cost)
        self.set_h_cost(self.h_cost)
        self.set_f_cost(self.f_cost)

    def set_g_cost(self, cost):
        self.g_cost = cost
        pygame.draw.rect(self.sprite.image, self.bgcolor, pygame.Rect(1, 1, self.side_length - 2, self.side_length - 2))
        self.sprite.image.blit(self.cost_font.render(str(math.ceil(self.g_cost)), True, (0, 0, 0)), (3, 0))

    def set_h_cost(self, cost):
        self.h_cost = cost
        self.sprite.image.blit(self.cost_font.render(str(math.ceil(self.h_cost)), True, (0, 0, 0)), (30, 0))

    def set_f_cost(self, cost):
        self.f_cost = cost
        self.sprite.image.blit(self.cost_font.render(str(math.ceil(self.f_cost)), True, (0, 0, 0)), (15, 20))

    def set_start(self, tf):
        if tf:
            self.is_start = True
            self.sprite.image.blit(self.sf_font.render('S', True, (0, 255, 0)), (15, 10))
        else:
            self.is_start = False
            pygame.draw.rect(self.sprite.image, 0xffffff, pygame.Rect(1, 1, self.side_length - 2, self.side_length - 2))

    def set_finish(self, tf):
        if tf:
            self.is_finish = True
            self.sprite.image.blit(self.sf_font.render('F', True, (255, 0, 0)), (15, 10))
        else:
            self.is_finish = False
            pygame.draw.rect(self.sprite.image, 0xffffff, pygame.Rect(1, 1, self.side_length - 2, self.side_length - 2))

    def toggle_blocking(self):
        if not self.is_start and not self.is_finish or self.is_blocking:
            self.is_blocking = not self.is_blocking
            if self.is_blocking:
                pygame.draw.rect(self.sprite.image, 0x000000,
                                 pygame.Rect(1, 1, self.side_length - 2, self.side_length - 2))
            else:
                pygame.draw.rect(self.sprite.image, 0xffffff,
                                 pygame.Rect(1, 1, self.side_length - 2, self.side_length - 2))


class TileSprite(pygame.sprite.Sprite):
    def __init__(self, parent):
        super(TileSprite, self).__init__()
        self.parent = parent

