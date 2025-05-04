import pygame
import math

class Rocket:

      def __init__(self, id):

        #Object Params
        self.id = id
        self.surface = pygame.Surface((self.size[0], self.size[1]), pygame.SRCALPHA)
        self.size = (50, 150)
        self.thrusters = {"right": 0, "left":0}

        #Physics Related
        self.angle = 90
        self.pos = (0.0,0.0) #x, y
        self.velocity = [0.0,0.0] #Vx , Vy
        self.acceleration = [0.0,0.0,0.0] #Ax, Ay, Aw

        #Initial functions
        self.drawRocket()

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

      def subAngle(self):
        self.angle -= 1

      def setThruster_L(self, state):
            self.thrusters["left"] = state
            if(state):
                self.addAngle()

      def setThruster_R(self, state):
            self.thrusters["right"] = state
            if(state):
                self.subAngle()

      def render(self, surface):
        #Get Surface Dimensions
        surfaceDim = surface.get_size()
        x = surfaceDim[0]/2
        y = surfaceDim[1]/2

        self.drawThrusters()
        rotated = pygame.transform.rotate(self.surface, self.angle)
        position = rotated.get_rect(center=(x,y))

        surface.blit(rotated, position)

      def drawRocket(self):
        pygame.draw.ellipse(self.surface, "red",(0,0,self.size[0],self.size[1]))
        pygame.draw.polygon(self.surface, "grey", [(0,140),(15, 150) ,(15,140), (10, 130)])
        pygame.draw.polygon(self.surface, "grey", [(50,140),(35, 150) ,(35,140), (40, 130)])
        pygame.draw.circle(self.surface, "grey" , (25, 50) , 10)
        pygame.draw.circle(self.surface, "blue" , (25, 50) , 7)
        pygame.draw.circle(self.surface, "grey" , (25, 90) , 10)
        pygame.draw.circle(self.surface, "blue" , (25, 90) , 7)

      def drawThrusters(self):
        if (self.thrusters["left"] == 1):
            pygame.draw.polygon(self.surface, "orange", [(0,140), (15,150), (0,150)])
        else:
            pygame.draw.polygon(self.surface, "blue", [(0,140), (15,150), (0,150)])

        if (self.thrusters["right"] == 1):
            pygame.draw.polygon(self.surface, "orange", [(50,140), (35,150), (50,150)])
        else:
            pygame.draw.polygon(self.surface, "blue", [(50,140), (35,150), (50,150)])

