import sys
sys.setrecursionlimit(10_000)

walls = []
start = None
end = None
length = 0
width = 0

minus = 100

with open("input.txt", "r", encoding="utf-8") as fichier:
    cptLine = 0
    for line in fichier:
        length = len(line)
        for index, char in enumerate(line):
            if char == '#': walls.append((cptLine, index))
            elif char == 'S': start = (cptLine, index)
            elif char == 'E': end = (cptLine, index)
        cptLine += 1
width = cptLine


            
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

path = {}
pathNotCheat = None

def find(pos, cheatWall, past):
    if not pos[0] in range(width) or not pos[1] in range(length):
        return
    
    if pos in walls:
        if cheatWall:
            return
        else:
            cheatWall = pos
    
    if pos in past:
        return
            
    if pathNotCheat and cheatWall and pos not in walls:
        if pos in pathNotCheat and len(past) <= pathNotCheat.index(pos) - minus:
            path[cheatWall] = past
        return
    
    if pos == end:
        path[cheatWall] = past
        return
    
    past = past.copy()
    past.append(pos)
    
    for dir in dirs:
        find((pos[0] + dir[0], pos[1] + dir[1]), cheatWall, past)
    
    
find(start, (0, 0), [])
pathNotCheat = path.pop((0, 0))

find(start, None, [])
print(len(path))