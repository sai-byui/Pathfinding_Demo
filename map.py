import pygame
from tile import Tile
from pathfinder import Pathfinder


class Map:
    def __init__(self, width, height, tile_side_length):
        self.start_tile = None
        self.finish_tile = None
        self.width = width
        self.height = height
        self.tiles = [height * [0] for _ in range(width)]
        self.tiles_unordered = []
        self.tile_images = pygame.sprite.Group()

        for x in range(width):
            for y in range(height):
                self.tiles[x][y] = Tile(x*tile_side_length, y*tile_side_length, tile_side_length)

        for col in self.tiles:
            for tile in col:
                self.tile_images.add(tile.sprite)
                self.tiles_unordered += [tile]

        self.establish_connections()

        self.pathfinder = Pathfinder(self.tiles_unordered, self.start_tile, self.finish_tile)

    def set_start_tile(self, tile):
        if not tile.is_finish:
            if self.start_tile:
                self.start_tile.set_start(False)
            tile.set_start(True)
            self.start_tile = tile
            self.pathfinder.start_node = tile
            if tile.is_blocking:
                tile.toggle_blocking()

    def set_finish_tile(self, tile):
        if not tile.is_start:
            if self.finish_tile:
                self.finish_tile.set_finish(False)
            tile.set_finish(True)
            self.finish_tile = tile
            self.pathfinder.finish_node = tile
            if tile.is_blocking:
                tile.toggle_blocking()

    def establish_connections(self):
        for x in range(self.width):
            for y in range(self.height):
                if x > 0:
                    self.tiles[x][y].connections += [self.tiles[x - 1][y]]
                    if y > 0:
                        self.tiles[x][y].connections += [self.tiles[x - 1][y - 1]]
                    if y < self.height - 1:
                        self.tiles[x][y].connections += [self.tiles[x - 1][y + 1]]
                if x < self.width - 1:
                    self.tiles[x][y].connections += [self.tiles[x + 1][y]]
                    if y > 0:
                        self.tiles[x][y].connections += [self.tiles[x + 1][y - 1]]
                    if y < self.height - 1:
                        self.tiles[x][y].connections += [self.tiles[x + 1][y + 1]]
                if y > 0:
                    self.tiles[x][y].connections += [self.tiles[x][y - 1]]
                if y < self.height - 1:
                    self.tiles[x][y].connections += [self.tiles[x][y + 1]]

