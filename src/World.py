import pygame
import random
from pygame.locals import *

class World:
    def __init__(self, height, width, id):
        self.height = height
        self.width = width
        self.block_h = 50
        self.block_w = 50
        self.blocks = [[0]*width]*height
        self.id = id

    #Import existing world line by line into this world's blocks
    def importWorld(self, filename):
        with open(filename) as world_file:

            #Split and convert string format to int and save to arrays
            world_load = []
            for line in world_file:
                world_load.append([int(block) for block in line.split(",")[:-1]])
            self.blocks = world_load




    #Save the existing world into a specific ID txt file
    def saveWorld(self):

        worldID = random.randint(0,2000000)
        with open(f"../worlds/world_{worldID}.txt", "w") as f:
            for line in self.blocks:
                string = ""
                for block in line:
                    string += str(block) + ","
                string += "\n"
                f.write(string)

    #Print the blocks array of the world
    def printBlocks(self):
        print(self.blocks)

    #Render each block according to its value
    def render(self, surface):

        for y in range(self.height):
            for x in range(self.width):
                match self.blocks[y][x]:
                    case 0:
                        pygame.draw.rect(surface, "blue", (x*self.block_w,y*self.block_h,self.block_w,self.block_h))
                    case 1:
                        pygame.draw.rect(surface, "gray", (x*self.block_w,y*self.block_h,self.block_w,self.block_h))
                    case _:
                        continue


