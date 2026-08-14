import pygame
from util import import_image
class Bullet(pygame.sprite.Sprite):
    def __init__(self,castle,  direction, groups):
        super().__init__(groups)
        self.castle = castle
        self.spawn_piont = (self.castle.rect.topleft[0], (self.castle.rect.y + self.castle.attack_source))
        self.image = import_image(['img', 'bullet.png'], 0.5)
        self.rect = self.image.get_rect(center =self.spawn_piont)