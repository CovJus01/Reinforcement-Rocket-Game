import pygame

class Rocket: 

  def __init__(self):
    self.pos = (0,0)
    self.size = (0, 0)
    self.angle = 0
    self.velocity = [0,0]

  def getPos(self):
    return self.pos
  
  def getSize(self):
    return self.size

  def getVelocity(self):
    return self.velocity

  def getAngle(self):
    return self.angle

  def setPosX(self, posX):
    self.pos[0] = posX
  
  def setPosY(self, posY):
    self.pos[1] = posY

  def setSize(self, size):
    self.size = size

  def setVelocity(self, velocity):
    self.velocity = velocity

  def setAngle(self, angle):
    self.angle = angle
  def render(self, surface):
    offset = self.size[0]/2
    surfaceDim = surface.get_size()
    x = surfaceDim[0]/2
    y = surfaceDim[1]/2
    pygame.draw.line(surface, "red" , (x, y-offset), (x, y+offset) , width = self.size[1])


