size = range(71)
walls = []
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cache = {}

with open("input.txt", "r", encoding="utf-8") as fichier:
    cpt = 0
    for line in fichier:
        if cpt == 1024:
            break
        wall = [int(x) for x in line.removesuffix("\n").split(",")]
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
    
move([{
    "pos": (0, 0),
    "value": 0
}])

print(cache[(70, 70)])
        
    