import sys
sys.setrecursionlimit(10_000)

walls = []

start = None
end = None

length = 0
width = 0

minus = 100
cheatValue = 20

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

cache = {}

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

def distEnd(pos, value):
    if not pos[0] in range(width) or not pos[1] in range(length) or pos in walls:
        return
    
    if pos in cache.keys() and cache[pos] < value:
        return
    
    cache[pos] = value
    
    for dir in dirs:
        distEnd((pos[0] + dir[0], pos[1] + dir[1]), value + 1)


def cheat(pos, value, cptPath):
    for i in range(-cheatValue, cheatValue + 1):
        diff = cheatValue - abs(i)
        for j in range(-diff, diff + 1):
            dist = abs(i) + abs(j)
            nextPos = (pos[0] + i, pos[1] + j)
            if nextPos in cache.keys() and cache[nextPos] - minus >= value + dist:
                cptPath += 1
    return cptPath


distEnd(end, 0)

cptPath = 0
for pos, value in cache.items():
    cptPath = cheat(pos, value, cptPath)
    
print(cptPath)