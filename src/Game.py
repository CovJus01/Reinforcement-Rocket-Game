import pygame
from pygame.locals import *
from EventHandler import EventHandler
from Rocket import Rocket
from Renderer import Renderer
from World import World


class Game:
    def __init__(self):
        self.running = False
        self.display_surface = None
        self.size = self.width, self.height = 1200, 900
        self.clock = pygame.time.Clock()
        self.rocket = Rocket(1)
        self.world = World(100,100,0)

    #Setup the game on it's full initialization
    def on_init(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self.running = True
        self.event_handler = EventHandler(self)
        self.renderer = Renderer(self.display_surface)
        self.world.importWorld("world_1794174.txt")
        self.renderer.addObject(self.world)
        self.renderer.addObject(self.rocket)

    #Run Game events
    def events(self):
        self.event_handler.updateEvents()
        self.event_handler.handleEvents()

    #Run Game logic
    def on_loop(self):
        self.event_handler.execEvents()

    #Run Game rendering
    def render(self):
        self.renderer.render()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self.running = False

        while (self.running):
            self.events()
            self.on_loop()
            self.render()
            self.clock.tick(60)
        self.on_cleanup()
