import pygame
from pygame.locals import *


class Renderer:
    def __init__(self, display_surface) :
        self.objects = {} #Object render function list
        self.objCount = 0 #Object Count
        self.display = display_surface

    #Add an object to the list
    def addObject(self, object):
        self.objects[object.id] = object.render
        self.objCount += 1

    #Remove an object from the renderer
    def removeObject(self, id):
        del self.objects[id]

    #The function that renders everything
    def render(self):
        #Render Background
        self.display.fill((67, 120, 180))
        #Render Objects over the background
        for key in self.objects:
            self.objects[key](self.display)
        pygame.display.flip()
