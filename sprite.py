import pygame
from util import import_image
class Bullet(pygame.sprite.Sprite):
    def __init__(self,castle,  direction, groups):
        super().__init__(groups)
        self.castle = castle
        # self.spawn_piont = (self.castle.rect.topleft[0], (self.castle.rect.y + self.castle.attack_source))
        self.image = import_image(['img', 'bullet.png'], 0.075)
        self.rect = self.image.get_rect(center =self.castle.castle_shoot_piont)
        self.direction = direction
        self.bullet_speed = 500
        
        
    def update(self, dt):
        print('update from bullet')
        print(self.direction)
        self.rect.center += self.direction * self.bullet_speed * dt