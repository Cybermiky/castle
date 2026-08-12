import pygame
from util import import_frames_dict
class enemy(pygame.sprite.Sprite):
    def __init__(self,x,y, health, enemy_type, enemy_data, *groups):
        super().__init__(*groups)
        self.x = x
        self.y = y
        self.health = health
        self.enemy_type = enemy_type
        self.enemy_data = enemy_data
        self.action ='walk'
        self.frame_index = 0
        self.enemy_frames = import_frames_dict('img','enemies', enemy_type)
        self.image = self.enemy_frames[self.action][self.frame_index]
        self.rect = self.image.get_rect(self.image, self,self.rect)
        # print(self.enemy_frames)
    
        
enemies_group = pygame.sprite.Group()
red_goblin= enemies(0,0,0,'red_goblin', 0, enemies_group)