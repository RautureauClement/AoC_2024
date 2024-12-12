blocks = []
garde = None
width = 0
length = 0
visit = []

avance = {
    'T': (-1, 0),
    'R': (0, 1),
    'B': (1, 0),
    'L': (0, -1)
}

with open("input.txt") as fichier:
    nbLine = 0
    for line in fichier:
        i = 0
        while True:
            pos = line.find("#", i)
            initGarde = line.find("^")
            if initGarde > 0:
                garde = {
                    'pos': (nbLine, initGarde),
                    'dir': 'T'
                }
            if pos == -1:
                break
            blocks.append((nbLine, pos))
            i = pos + 1
            width = max(width, pos)
        nbLine += 1
    length = nbLine - 1
    

def turn():
    dirs = ['T', 'R', 'B', 'L']
    dir = garde['dir']
    
    garde['dir'] = dirs[(dirs.index(dir) + 1) % 4]

visit.append(garde["pos"])

while garde["pos"][0] in range(length + 1) and garde["pos"][1] in range(width + 1):
    gp = garde['pos']
    dir = garde['dir']
    
    futur = (gp[0] + avance[dir][0], gp[1] + avance[dir][1])
    
    if futur in blocks:
        turn()
    else:
        garde['pos'] = futur
        if not futur in visit:
            visit.append(futur)
    
print(len(visit) -1)