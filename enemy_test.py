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
        self.surface = pygame.display.get_surface()
        
        
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
        self.animation_speed = 25
        self.collided = False
        self.is_attacking = False
    
        self.rect = self.image.get_frect(bottomleft =(self.x , self.castle.rect.bottomleft[1]))
        self.hitbox_rect = self.rect.inflate(-25, -10) 
        self.hitbox_offset = vector(int(self.image.get_width()*0.55)//2,0)
        self.hitbox_rect.center = self.rect.center - self.hitbox_offset
       
        
        
  
    def get_direction(self):
     
            
            target = vector(
                self.castle.rect.left - self.hitbox_rect.width / 2,
                self.castle.rect.bottomleft[1] * 0.9
            )

            total_vector = target - vector(self.hitbox_rect.center)

            if total_vector.length() > 4:
                            direction = total_vector.normalize()
            else:
                direction =vector(0, 0)
                self.is_attacking = True

            return total_vector, direction
    def collision(self):
        total_vector = self.get_direction()[0]
        
        if total_vector.length() < 4:
            # print('collison kicked in')
            self.collided = True
            if self.hitbox_rect.right >= self.castle.rect.left:
                self.hitbox_rect.right = self.castle.rect.left
                # self.rect.center = self.hitbox_rect.center
                self.rect.center =  self.hitbox_rect.center + self.hitbox_offset
        else: 
            self.collided = False
            
            
    def move_to_castle(self, dt):
        if not self.is_attacking:
            self.hitbox_rect.center += self.get_direction()[1] * self.animation_speed * dt
            self.rect.center =  self.hitbox_rect.center + self.hitbox_offset
    def animate(self, dt):
        self.frame_index+= self.animation_speed*dt
        if(self.frame_index > len(self.enemy_frames[self.action])-1):
            self.frame_index = 0
        self.image =  self.enemy_frames[self.action][int(self.frame_index)]
    def draw(self):
        self.surface.blit(self.image, self.rect)
        
        pygame.draw.rect(self.surface, 'red',self.rect, 3)
        pygame.draw.rect(self.surface, 'green',self.hitbox_rect, 3)
    def attack_castle(self):
            if self.is_attacking:
                self.action = 'attack'
                print('attacking')
        
    
    def update(self, dt):
        self.move_to_castle(dt)
        self.collision()
        self.attack_castle()
        self.animate(dt)
    
        
enemies_group = pygame.sprite.Group()
