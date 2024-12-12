map = []

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        map.append([int(x) for x in line if x != '\n'])
        
width = range(len(map[1]))
heigth = range(len(map))

deplacements = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def canUp(pos, last):
    if not pos[0] in heigth or not pos[1] in width:
        return []
    
    current = map[pos[0]][pos[1]]
    
    if current - last != 1:
        return []
    if current == 9:
        return [pos]
    
    ninePos = []
    for deplacement in deplacements:
       for new in canUp((pos[0] + deplacement[0], pos[1] + deplacement[1]), current):
            ninePos.append(new)
    return ninePos
    
sum = 0

for i in heigth:
    for j in width:
        sum += len(canUp((i, j), -1))
        
print(sum)