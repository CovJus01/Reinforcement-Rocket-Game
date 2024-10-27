import pygame 

class EventHandler:

  def __init__(self, game):
    self.events_processed = 0
    self.eventList = []
    self.game = game

  def updateEvents(self):
    self.eventList = pygame.event.get()

  def handleEvents(self):
    for event in self.eventList:
      match event.type:
        case pygame.QUIT:
          self.game.running = False
        case pygame.KEYDOWN:
          self.handleKEYDOWN(event)
        case _:
          print(event.type)

  def handleKEYDOWN(self, event):
    match event.key:
      case pygame.locals.K_BACKSPACE:
        pygame.draw.line(self.game.display_surface, "red" , (450, 200), (450, 450) , width = 1)
      case _:
        print(event.key)



