import random
#Setting blocktypes to reduce variable size
# 0 is no block, others represent various blocks

blockTypes = [0b00, 0b01, 0b10, 0b11]

class World:

    def __init__(self, size):
        self.size = size
        self.coefficients = [1]
        self.world = [[ blockTypes[0] for i in range(size[1])] for i in range(size[0]) ]
        self.channel = 4

    def generateWorld(self):
        for x, yarray in enumerate(self.world):
            current_point = (x, x*coefficients[0])
            range_one = -1
