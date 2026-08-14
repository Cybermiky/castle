import pygame
from pygame import Vector2 as vector
from settings import resource_font,screen_width
from util import import_image
class Button_menu():
    def  __init__(self, imagePath, y,multiplier, display_info,scale):
        self.font = resource_font
        # imagePathExample = ['img','repair.png']
        self.distance =100
        self.x = int(screen_width *0.65) +(self.distance * multiplier)
        self.y = 15
        self.scale = scale
        self.display_surface = pygame.display.get_surface()
        self.image = import_image(imagePath, self.scale)
        self.rect = self.image.get_rect(topleft = (self.x,self.y))
        self.displayInfo = display_info
        self.clicked = False
    
    def draw_menu(self):
        self.display_surface.blit(self.image,self.rect)
        font_surface =self.font.render(f'{self.displayInfo}',True,'purple')
        font_rect = font_surface.get_rect(midtop =(vector(self.rect.midbottom)+ vector(self.image.get_width()//2-10,7)))
        self.display_surface.blit(font_surface, font_rect)
    def check_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        # print(list(pygame.MOUSEBUTTONDOWN(0)))
        left_mouse_clicked =pygame.mouse.get_just_pressed()[0]
        
        if self.rect.collidepoint(mouse_pos[0], mouse_pos[1]) and left_mouse_clicked and not self.clicked:
            # print('clicked')
            self.clicked = True
            
        else:
            # print('not in image or already clicked')
            self.clicked= False
        
        # return self.clicked
    def update(self):
        self.check_clicked()
        