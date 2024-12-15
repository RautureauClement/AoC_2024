class Robot:
    size = (101, 103)
    quarts = [
            (range((size[0] - 1) // 2),                 range((size[1] - 1) // 2)),
            (range((size[0] - 1) // 2 + 1, size[0]),    range((size[1] - 1) // 2)),
            (range((size[0] - 1) // 2),                 range((size[1] - 1) // 2 + 1, size[1])),
            (range((size[0] - 1) // 2 + 1, size[0]),    range((size[1] - 1) // 2 + 1, size[1]))
        ]
    
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
    
    def deplace(self, sec):
        self.pos = (
            (self.pos[0] + self.vel[0] * sec ) % self.size[0],
            (self.pos[1] + self.vel[1] * sec ) % self.size[1]
        )
        
    def getQuart(self):
        for index, quart in enumerate(self.quarts):
            if self.pos[0] in quart[0] and self.pos[1] in quart[1]:
                return index
        
        return None

quarts = [0, 0, 0, 0]
with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        posStr, velStr = line.removesuffix('\n').split(' ')
        pos = [int(x) for x in posStr[2:].split(',')]
        vel = [int(x) for x in velStr[2:].split(',')]
        
        robot = Robot(pos, vel)
        robot.deplace(100)
        quart = robot.getQuart()
        if quart != None:
            quarts[quart] += 1
        
mul = 1
for quart in quarts:
    mul *= quart
    
print(mul)