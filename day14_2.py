class Robot:
    size = (101, 103)
    
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
    
    def deplace(self, sec):
        self.pos = (
            (self.pos[0] + self.vel[0] * sec ) % self.size[0],
            (self.pos[1] + self.vel[1] * sec ) % self.size[1]
        )

robots = []
with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        posStr, velStr = line.removesuffix('\n').split(' ')
        pos = [int(x) for x in posStr[2:].split(',')]
        vel = [int(x) for x in velStr[2:].split(',')]
        
        robot = Robot(pos, vel)
        robots.append(robot)

cpt = 0
while True:
    map = [[" " for _ in range(Robot.size[0])] for _ in range(Robot.size[1])]
    same = False
    for robot in robots:
        if map[robot.pos[1]][robot.pos[0]] == 'X':
            same = True
        map[robot.pos[1]][robot.pos[0]] = "X"
        robot.deplace(1)
    cpt += 1
    if same:
        continue
    for line in map:
        print("".join(line))
    break