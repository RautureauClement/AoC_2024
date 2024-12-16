walls = []
boxs = []
robot = None

firstPart = True

dirs = {
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1],
    "^": [-1, 0]
}

def move(dir, object):
    futur = [object[0] + dir[0], object[1] + dir[1]]
    if futur in walls:
        return object
    if futur in boxs:
        ind = boxs.index(futur)
        box = boxs[ind]
        boxs[ind] = move(dir, box)
    if futur in boxs:
        return object
    return futur

with open("input.txt", "r", encoding="utf-8") as fichier:
    cptLine = 0
    for line in fichier:
        if line == '\n':
            firstPart = False
            continue
        line = line.removesuffix('\n')
        
        if firstPart:
            for index, char in enumerate(line):
                if char == '#':
                    walls.append([cptLine, index])
                elif char == "@":
                    robot = [cptLine, index]
                elif char == 'O':
                    boxs.append([cptLine, index])
            cptLine += 1
        else:
            for char in line:
                robot = move(dirs[char], robot)

sum = 0
for box in boxs:
    sum += box[0] * 100 + box[1]
print(sum)
