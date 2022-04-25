import pygame
from app.player import Player
from app.settings import *
from app.tile import Tile


class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprites group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        # sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites,
                         self.obstacles_sprites])
                if col == 'p':
                    Player((x, y), [self.visible_sprites])

    def run(self):

        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
