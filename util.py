import pygame
pygame.init()
window = pygame.display.get_surface()
from data import ENEMIES_DATA
from os.path import join, splitext,basename
from os import walk

def import_image_frames(*path,scale =1, transparent = True):
    frames = []
   
    for index , (paths, folders , images) in enumerate(walk(join(*path))):
        
        if index == 0 and images:
            for image in sorted(images, key = lambda image: -int(image.split('.')[0].split('_')[1])):
                # print(join(paths, image))
                # surface = pygame.image.load(join(paths, image)).convert_alpha() if transparent else pygame.image.load(join(paths, image)).convert()
                # .convert_alpha() if transparent else pygame.image.load(join(paths, image)).convert()
                surface = pygame.image.load(join(paths, image))
                new_scale_width = int(surface.get_width()*scale)
                new_scale_height = int(surface.get_height()*scale)
                # print(new_scale_width,new_scale_height  )
                scaled_surface = pygame.transform.scale(surface, (new_scale_width, new_scale_height))
                frames.append(scaled_surface)
        
    return frames
def sort_image(image_sprite):
   
    return  int(splitext(image_sprite)[0])
    
def import_frames_dict(path_array,scale =1, transparent = True):
    frames = {}


   
    for index , (paths, folders , images) in enumerate(walk(join(*path_array))):
        
        if index == 0:
            for folder in folders:
                frames[folder] =[]
        else:
            image_list= []
            
            for image in sorted(images, key=  sort_image):
                         
                           
                            surface = pygame.image.load(join(paths, image))
                            new_scale_width = int(surface.get_width()*scale)
                            new_scale_height = int(surface.get_height()*scale)
                            # print(new_scale_width,new_scale_height  )
                            scaled_surface = pygame.transform.scale(surface, (new_scale_width, new_scale_height))
                            image_list.append(scaled_surface)
            
            action = basename(paths)
            frames[action]= image_list
    return frames
            
    # print(frames)
        
            
        
    

def import_image(*path,scale =1, transparent = True):
    # print(str(list(*path)) +'from import image')
    surface = pygame.image.load(join(*path))
    # surface = pygame.image.load(join(*path)).convert_alpha() if transparent else pygame.image.load(join(*path)).convert()
    new_scale_width = int(surface.get_width()*scale)
    new_scale_height = int(surface.get_height()*scale)
    # print(new_scale_width,new_scale_height  )
    scaled_surface = pygame.transform.scale(surface, (new_scale_width, new_scale_height))
    return scaled_surface

array =  ENEMIES_DATA['red_goblin']['path']
print(array)
