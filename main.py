
import pygame
import sys
from data import ENEMIES_DATA
from settings import *
from util import import_image, import_image_frames ,import_frames_dict
from enemy_test import enemy
from timer import Timer
from button_menu import Button_menu
from sprite import Bullet

pygame.init()
class castle():
    def __init__(self,  scale, health):
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
        self.shoot_countdown = 300
    def shoot_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print('castle shooting')
    def shoot_enemies(self):
        castle_shoot_piont = (self.rect.topleft[0], (self.rect.y + self.attack_source))
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.line(self.display_surface, 'red', castle_shoot_piont, mouse_pos, 3)
    
        source = self.attack_source
        target = mouse_pos
        
        #             total_vector = target - vector(self.hitbox_rect.center)
        
       
    def draw(self):
        self.display_surface.blit(self.image, self.rect)
        pygame.draw.rect(self.display_surface, 'blue',self.rect, 3)
        self.shoot_enemies()
    def update(self):
        # self.shoot_enemies()
        self.shoot_input()
        pass
        
# print(screen_width, screen_height)
class Castle_defender():
    def __init__(self):
        self.display_suface = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Castle Defense")
        self.running = True
        self.clock = pygame.time.Clock()
        self.bg = import_image(['img','bg.png'])
        self.Castle = castle(0.2, 1000)
        self.health_menu1 = Button_menu(['img','repair.png' ], 20,0, '1000',0.6)
        # self.health_menu2 = Button_menu(['img','repair.png' ], 20,1, '1000')
        # self.health_menu3= Button_menu(['img','repair.png' ], 20,2, '1000')
        self.enemies_group = pygame.sprite.Group()
        self.bullets_group = pygame.sprite.Group()
        self.enemy1 = enemy(100, screen_height -100,'goblin', self.Castle, self.enemies_group)
        self.bullet1 = Bullet(self.Castle,(0,0),self.bullets_group)
        # self.spawn_enemies = Timer(1000,self.spaw_enemies_func,autostart=True, one_time=False)
        # self.spawn_enemies.activate()
        
    
        
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
            # self.enemies_group.update(dt)
            
            self.enemy1.update(dt)
            self.Castle.update()
            
                    
                    
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