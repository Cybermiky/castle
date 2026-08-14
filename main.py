
import pygame
import sys
from data import ENEMIES_DATA
from settings import *
from util import import_image, import_image_frames ,import_frames_dict
from enemy_test import enemy
from timer import Timer
from button_menu import Button_menu
from sprite import Bullet
from pygame import Vector2 as vector
pygame.init()
class castle():
    def __init__(self,  scale, health, shoot_bullet_func):
        self.x = screen_width-250
        self.y = screen_height- 300
        self.frames = import_image_frames('img', 'castle',scale=0.2)
        self.frame_index =0
        self.image = self.frames[self.frame_index]
        # self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.rect = self.image.get_rect()
        self.rect.x =  self.x
        self.rect.y = self.y
        self.display_surface = pygame.display.get_surface()
        self.attack_source = (self.image.get_height() *0.35)
        self.attack_source_vector  = (self.rect.x, self.attack_source)
        self.shoot_countdown = 500
        self.max_shoot_countdown= self.shoot_countdown
        self.castle_shoot_piont = (self.rect.topleft[0], (self.rect.y + self.attack_source))
        self.countdown_speed = 10
        self.can_shoot = True
        self.shoot_bullet_func = shoot_bullet_func
    def shoot_input(self,dt):
  
        if not self.can_shoot:
            self.shoot_countdown -= self.countdown_speed * dt 
            if self.shoot_countdown <=0 : 
                self.shoot_countdown = self.max_shoot_countdown
                self.can_shoot = True
        
        # keys = pygame.key.get_pressed() 
        left_mouse_clicked =pygame.mouse.get_just_pressed()[0]
        if left_mouse_clicked and self.can_shoot:
            print('listening for shoot input')
            direction = self.shoot_direction()
            self.shoot_bullet_func(self,direction)
            self.can_shoot= False
    def shoot_direction(self):
        castle_shoot_piont = self.castle_shoot_piont
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(self.display_surface, 'red', castle_shoot_piont, mouse_pos, 3)
        source = castle_shoot_piont
        target = mouse_pos
        direction = vector(target)-vector(source)
        norm_direction = direction.normalize() if direction.length() > 3 else vector(-1,1)
        
        return norm_direction
        
       
    def draw(self):
        self.display_surface.blit(self.image, self.rect)
        pygame.draw.rect(self.display_surface, 'blue',self.rect, 3)
    
    def update(self, dt):
        # self.shoot_enemies()
        self.shoot_input(dt)
        
        
# print(screen_width, screen_height)
class Castle_defender():
    def __init__(self):
        self.display_suface = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Castle Defense")
        self.running = True
        self.clock = pygame.time.Clock()
        self.bg = import_image(['img','bg.png'])
        self.Castle = castle(0.2, 1000, self.shoot_bulllet)
        self.health_menu1 = Button_menu(['img','repair.png' ], 20,0, '1000',0.6)
     
        self.enemies_group = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()
        self.enemy1 = enemy(100, screen_height -100,'goblin', self.Castle, self.enemies_group)
    
    def shoot_bulllet(self, castle, direction):
        print("shoot bullet")
        Bullet(castle,direction, self.bullets_group)
    
        
    def run(self):
        while self.running:
            dt = self.clock.tick(-1)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
            # timer
            # self.spawn_enemies.update()
            # update
           
            
            # self.enemy1.update(dt)
            self.Castle.update(dt)
            self.enemies_group.update(dt)
            self.bullets_group.update(dt)
            
                    
                    
            #  draw       
            self.display_suface.blit(self.bg, (0,0))
            self.Castle.draw()
            # self.enemies_group.draw(self.display_suface)
            self.enemy1.draw()
            self.health_menu1.draw_menu()
            self.bullets_group.draw(self.display_suface)
            
            # check if user clicked
            self.health_menu1.check_clicked()
            
            
        
            pygame.display.update()

if __name__ == '__main__':
    game = Castle_defender()
    
    game.run()