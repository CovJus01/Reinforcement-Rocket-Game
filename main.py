import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.running = True
        self.display_surface = None
        self.size = self.width, self.height = 1200, 900
    
    def on_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self.running = True
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.locals.K_BACKSPACE:
                pygame.draw.line(self.display_surface, "red", (450,200), (450,450), width = 20)

      
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
                for event in pygame.event.get():
                    self.on_event(event)
                self.on_loop()
                self.on_render()
                self.clock.tick(60)
        self.on_cleanup()



if __name__ == "__main__" :
  theApp = Game()
  theApp.on_execute()