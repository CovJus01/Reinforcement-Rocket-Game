import pygame


class EventHandler:

    def __init__(self, game):
        self.events_processed = 0
        self.eventList = []
        self.game = game
        self.eventStates = {
          "KEY_D": {"val": False, "function": self.game.rocket.subAngle},
          "KEY_A": {"val": False, "function": self.game.rocket.addAngle}
        }

    def updateEvents(self):
        self.eventList = pygame.event.get()

    def handleEvents(self):
        for event in self.eventList:
            match event.type:
                case pygame.QUIT:
                    self.game.running = False
                case pygame.KEYDOWN:
                    self.handleKEYDOWN(event)
                case pygame.KEYUP:
                    self.handleKEYUP(event)
                case _:
                    pass

    def handleKEYDOWN(self, event):
        match event.key:
            case pygame.locals.K_a:
                self.eventStates["KEY_A"]["val"] = True
            case pygame.locals.K_d:
                self.eventStates["KEY_D"]["val"] = True

    def handleKEYUP(self, event):
        match event.key:
            case pygame.locals.K_a:
                self.eventStates["KEY_A"]["val"] = False
            case pygame.locals.K_d:
                self.eventStates["KEY_D"]["val"] = False
            case _:
                pass

    def execEvents(self):
        for event in self.eventStates:
            if (self.eventStates[event]["val"]):
                self.eventStates[event]["function"]()
