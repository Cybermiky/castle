import pygame
pygame.init()
from os.path import join
from os import walk
def import_image_frames(*path,scale =1, transparent = True):
    frames = []
   
    for index , (paths, folders , images) in enumerate(walk(join(*path))):
        
        if index == 0 and images:
            for image in sorted(images, key = lambda image: -int(image.split('.')[0].split('_')[1])):
                print(join(paths, image))
                surface = pygame.image.load(join(paths, image))
                # .convert_alpha() if transparent else pygame.image.load(join(paths, image)).convert()
                new_scale_width = int(surface.get_width()*scale)
                new_scale_height = int(surface.get_height()*scale)
                # print(new_scale_width,new_scale_height  )
                scaled_surface = pygame.transform.scale(surface, (new_scale_width, new_scale_height))
                frames.append(scaled_surface)
        
    return frames

def import_image(*path,scale =1, transparent = True):
    # print(str(list(*path)) +'from import image')
    surface = pygame.image.load(join(*path)).convert_alpha() if transparent else pygame.image.load(join(*path)).convert()
    new_scale_width = int(surface.get_width()*scale)
    new_scale_height = int(surface.get_height()*scale)
    # print(new_scale_width,new_scale_height  )
    scaled_surface = pygame.transform.scale(surface, (new_scale_width, new_scale_height))
    return scaled_surface

print(import_image_frames('img','castle',scale = 1, transparent = True))
    