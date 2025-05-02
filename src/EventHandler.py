import pygame


class EventHandler:

    def __init__(self, game):
        self.events_processed = 0
        self.eventList = []
        self.game = game
        self.eventStates = {
          "KEY_D": {"val": 0, "function": self.game.rocket.setThruster_R},
            "KEY_A": {"val": 0, "function": self.game.rocket.setThruster_L}
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
                self.eventStates["KEY_A"]["val"] = 1
            case pygame.locals.K_d:
                self.eventStates["KEY_D"]["val"] = 1

    def handleKEYUP(self, event):
        match event.key:
            case pygame.locals.K_a:
                self.eventStates["KEY_A"]["val"] = 0
            case pygame.locals.K_d:
                self.eventStates["KEY_D"]["val"] = 0
            case _:
                pass

    def execEvents(self):
        for event in self.eventStates:
            self.eventStates[event]["function"](self.eventStates[event]["val"])
