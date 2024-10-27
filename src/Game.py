import pygame
from pygame.locals import *

from EventHandler import EventHandler


class Game:
    def __init__(self):
        self.running = True
        self.display_surface = None
        self.size = self.width, self.height = 1200, 900
        self.clock = pygame.time.Clock()
        self.event_handler = EventHandler(self)

    def on_init(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self.running = True
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            self.handleKEYDOWN(event)

    def on_loop(self):
        pass
    
    def on_render(self):
        pygame.display.flip()
    
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while( self.running ):
                self.event_handler.updateEvents()
                self.event_handler.handleEvents()
                self.on_loop()
                self.on_render()
                self.clock.tick(60)
        self.on_cleanup()
