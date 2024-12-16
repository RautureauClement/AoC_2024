import sys
import time

paths = {}
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start = None
end = None

size = (17, 17)
size = (141, 141)

with open("input.txt", "r", encoding="utf-8") as fichier:
    cptLine = 0
    for line in fichier:
        for index, char in enumerate(line):
            if char in '.SE':
                paths[(cptLine, index)] = {
                    "value": sys.maxsize,
                    "side": []
                }
            if char == 'S':
                start = (cptLine, index)
            elif char == 'E':
                end = (cptLine, index)
                
        cptLine += 1

for key, path in paths.items():
    for dir in dirs:
        pos = (key[0] + dir[0], key[1] + dir[1])
        if pos in paths.keys():
            path['side'].append(pos)

def find(cases):
    next = []
    for case in cases:
        path = paths[case['path']]
        if path['value'] < case['value']:
            continue
        
        path['value'] = case['value']
        
        if case['path'] == end:
            continue
        
        for side in path['side']:
            diff = (side[0] - case['path'][0], side[1] - case['path'][1])
            rotate = 0 if diff == case['dir'] else 1000
            next.append({
                'path': side,
                'dir' : diff,
                'value': case['value'] + 1 + rotate
            })
    if len(next) == 0:
        return
    find(next)
    
def getPath(cases, set):
    next = []
    for n in cases:
        if not n in set:
            set.append(n)
    for case in cases:
        path = paths[case]
        for side in path['side']:
            if side in set:
                continue
            sideObj = paths[side]
            diff = path['value'] - sideObj['value']
            if diff < 0 and (diff != -999 or case == end):
                continue
            if not side in next:
                next.append(side)
    
    if len(next) == 0:
        return set
    
    return getPath(next, set)
        
        
find([{'path': start, 'dir' : (0, 1), 'value': 0}])

res = getPath([end], [])

map = [["#" for _ in range(size[0])] for _ in range(size[1])]

for p in paths.keys():
    map[p[0]][p[1]] = ' '
for r in res:
    map[r[0]][r[1]] = 'o'
    
    
for line in map:
    print("".join(line))
    
print(len(res))