import pygame
from util import import_frames_dict
from data import ENEMIES_DATA
from pygame.math import Vector2 as vector
class enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,  enemy_type,castle, groups):
        super().__init__(groups)
        self.x = x
        self.y = y
        self.scale = 0.2
        self.castle = castle
        
        self.enemy_type = enemy_type
        # self.enemy_data = enemy_data
        self.action ='walk'
        self.frame_index = 0
        # print('hi...................................')
        # print(enemy_type, enemy_data)
        
        self.enemy_frames = import_frames_dict(ENEMIES_DATA[enemy_type]['path'], scale=self.scale)
        
  
        # print(self.enemy_frames)
        
        self.health =  ENEMIES_DATA[enemy_type]['health']
        # print('health ', self.health)
        self.image = self.enemy_frames[self.action][self.frame_index]
        self.animation_speed = 45
        # self.image = pygame.surface.Surface((100,100))
        # self.image.fill('red')
        self.rect = self.image.get_frect(bottomleft =(self.x , self.castle.rect.bottomleft[1]))
        # self.rect.bo
        
        
        # print(self.enemy_frames)
    def get_direction(self):
        total_vector = (vector(self.castle.rect.bottomleft) *vector(1, 0.9)) - vector(self.rect.center)
        direction = total_vector.normalize() if total_vector.length() > 0 else total_vector
        return direction
    def move_to_castle(self, dt):
        self.rect.center += self.get_direction() * self.animation_speed * dt
    def animate(self, dt):
        self.frame_index+= self.animation_speed*dt
        if(self.frame_index > len(self.enemy_frames[self.action])-1):
            self.frame_index = 0
        self.image =  self.enemy_frames[self.action][int(self.frame_index)]
    def update(self, dt):
        self.move_to_castle(dt)
        self.animate(dt)
    
        
enemies_group = pygame.sprite.Group()
