import pygame
import math

class Rocket: 

  def __init__(self):
    self.pos = (0,0) #x, y
    self.size = (400, 2)
    self.angle = 90
    self.velocity = [0,0] #Vx , Vy
    self.acceleration = [0,0,0] #Ax, Ay, Aw
    self.head = (0,0)
    self.tail = (0,0)

  def getPos(self):
    return self.pos
  
  def getSize(self):
    return self.size

  def getVelocity(self):
    return self.velocity

  def getAcceleration(self):
    return self.acceleration

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

  def setAcceleration(self, acceleration):
    self.acceleration = acceleration
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
