
import pygame
import sys
from settings import *
from util import import_image, import_image_frames ,import_frames_dict
from enemy import enemy

pygame.init()
class castle():
    def __init__(self,  scale, health):
        self.x = screen_width-250
        self.y = screen_height- 300
        self.frames = import_image_frames('img', 'castle',scale=0.2)
        self.frame_index =0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.display_surface = pygame.display.get_surface()
    def draw(self):
        self.display_surface.blit(self.image, self.rect)
        
# print(screen_width, screen_height)
class Castle_defender():
    def __init__(self):
        self.window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Castle Defense")
        self.running = True
        self.bg = import_image('img','bg.png')
        self.Castle = castle(0.2, 1000)
        self.enemies_group = pygame.sprite.Group()
        self.enemy1 = enemy()
        
        
        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()
                    
                    
                    
            self.window.blit(self.bg, (0,0))
            self.Castle.draw()
        
            pygame.display.update()

if __name__ == '__main__':
    game = Castle_defender()
    
    game.run()