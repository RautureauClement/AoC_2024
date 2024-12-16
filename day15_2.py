import time

walls = []
boxs = []
robot = None
size = (50, 100)
# size = (10, 20)
firstPart = True

dirs = {
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1],
    "^": [-1, 0]
}

def moveBox(dir, indexs):
    if len(indexs) == 0:
        return True
    nexMove = []
    for index in indexs:
        for i in range(2):
            futur = [boxs[index][i][0] + dir[0], boxs[index][i][1] + dir[1]]
            if futur in walls:
                return False
            
            for ind, boxx in enumerate(boxs):
                if ind == index:
                    continue
                
                if futur in boxx:
                    if not ind in nexMove:
                        nexMove.append(ind)
                    break
        
    if not moveBox(dir, nexMove):
        return False
    
    for index in indexs:
        boxs[index] = [
            [boxs[index][0][0] + dir[0], boxs[index][0][1] + dir[1]],
            [boxs[index][1][0] + dir[0], boxs[index][1][1] + dir[1]]
        ]
    
    return True
        
        

def move(dir, robot):
    futur = [robot[0] + dir[0], robot[1] + dir[1]]
    if futur in walls:
        return robot
    box = None
    indexBox = None
    for index, boxx in enumerate(boxs):
        if futur in boxx:
            box = boxx
            indexBox = index
            break
    
    if box == None:
        return futur
    
    moveBox(dir, [indexBox])
    
    if futur in boxs[indexBox]:
        return robot
    return futur

def printMap():
    map = [[" " for _ in range(size[1])] for _ in range(size[0])]
    for wall in walls:
        map[wall[0]][wall[1]] = "#"
    for box in boxs:
        map[box[0][0]][box[0][1]] = "["
        map[box[1][0]][box[1][1]] = "]"
    map[robot[0]][robot[1]] = "@"
    
    for line in map:
        print("".join(line))

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
                    walls.extend([[cptLine, index * 2], [cptLine, index * 2 + 1]])
                elif char == "@":
                    robot = [cptLine, index * 2]
                elif char == 'O':
                    boxs.append([[cptLine, index * 2], [cptLine, index * 2 + 1]])
            cptLine += 1
        else:
            for char in line:
                robot = move(dirs[char], robot)
                printMap()
                time.sleep(0.05)


printMap()
sum = 0
for box in boxs:
    
    sum += box[0][0] * 100 + box[0][1]
print(sum)