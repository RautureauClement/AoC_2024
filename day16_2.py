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
        
find([{'path': start, 'dir' : (0, 1), 'value': 0}])

print(paths[end])