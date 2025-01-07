import sys
sys.setrecursionlimit(2000)

size = range(71)
end = (70, 70)
wait = 1024


walls = []
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
wallsFall = []

cache = {}

path = []

with open("input.txt", "r", encoding="utf-8") as fichier:
    cpt = 0
    for line in fichier:
        wall = [int(x) for x in line.removesuffix("\n").split(",")]
        if cpt >= wait:
            wallsFall.append((wall[0], wall[1]))
        else:
            walls.append((wall[0], wall[1]))
        cpt += 1
       
def move(cases):
    next = []
    for case in cases:
        pos = case["pos"]
        if not pos[0] in size or not pos[1] in size or pos in walls:
            continue
        
        if pos in cache.keys() and cache[pos] < case['value']:
            continue
        
        cache[pos] = case["value"]
        for dir in dirs:
            n = {
                "pos" : (pos[0] + dir[0], pos[1] + dir[1]),
                "value": case["value"] + 1
            }
            if not n in next :
                next.append(n)
    if len(cases) == 0:
        return
    move(next)
    
def getPath(pos, path):
    if pos == (0, 0):
        path.append((0, 0))
        return path
    
    path.append(pos)
    value = cache[pos]
    for dir in dirs:
        next = (pos[0] + dir[0], pos[1] + dir[1])
        if next in cache.keys() and cache[next] + 1 == value:
           return getPath(next, path)
        
move([{
    "pos": (0, 0),
    "value": 0
}])

path = getPath(end, [])
for pos in wallsFall:
    walls.append(pos)
    if not pos in path:
        continue
    
    cache = {}
    move([{
        "pos": (0, 0),
        "value": 0
    }])

    if not end in cache.keys():
        print(pos)
        break
    path = getPath(end, [])
        