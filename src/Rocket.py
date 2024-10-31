import pygame
import math

class Rocket: 

  def __init__(self):
    self.pos = (0,0)
    self.size = (400, 200)
    self.angle = 0
    self.velocity = [0,0]
    self.head = (0,0)
    self.tail = (0,0)

  def on_init(self):
    self.setAngle(0)
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

  def addAngle(self):
    self.angle += 1
    self.updatePoints()

  def subAngle(self):
    self.angle -= 1 
    self.updatePoints()

  def render(self, surface):
    surfaceDim = surface.get_size()
    x = surfaceDim[0]/2
    y = surfaceDim[1]/2
    pygame.draw.line(surface, "red" , (x+self.head[0], y-self.head[1]), (x+self.tail[0], y-self.tail[1]) , width = self.size[1])

  def updatePoints(self):
    radius = self.size[0]/2
    self.head = (int(radius*math.cos(math.radians(self.angle))), int(radius*math.sin(math.radians(self.angle))))
    self.tail = (-self.head[0], -self.head[1])
