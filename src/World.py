
class World:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.blocks = [[0]*width]*height

    def print_blocks(self):
        print(self.blocks)

    def render(self, surface):
        #Get Surface Dimensions
        surfaceDim = surface.get_size()
        x = surfaceDim[0]/2
        y = surfaceDim[1]/2

        #Draw the line on the surface with the values
        pygame.draw.line(surface,
                         "red" ,
                         (x+self.head[0], y-self.head[1]),
                         (x+self.tail[0], y-self.tail[1]),
                         width = self.size[1])

    def updatePoints(self):
        radius = self.size[0]/2
        #Calculate the points of the head
        self.head = (int(radius*math.cos(math.radians(self.angle))),
                     int(radius*math.sin(math.radians(self.angle))))
        #Tail points are the negative values of the head
        self.tail = (-self.head[0], -self.head[1])


