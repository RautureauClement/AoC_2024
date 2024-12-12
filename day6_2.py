blocks = []
garde = None
gardeInit = None
width = 0
length = 0
dirs = ['T', 'R', 'B', 'L']

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
                gardeInit = (nbLine, initGarde)
            if pos == -1:
                break
            blocks.append((nbLine, pos))
            i = pos + 1
            width = max(width, pos)
        nbLine += 1
    length = nbLine - 1
    

def turn():
    dir = garde['dir']
    
    garde['dir'] = dirs[(dirs.index(dir) + 1) % 4]
cpt = 0

boucle = (length+1) * (width + 1)

for i in range(length + 1):
    for j in range(width + 1):
        print((i * (length +1) + j) * 10000 // boucle / 100)
        newBlock = (i, j)
        if newBlock in blocks:
            continue
        
        blocks.append(newBlock)
        
        garde = {
            'pos': gardeInit,
            'dir': 'T'
        }
        visit = [garde["pos"] + (garde['dir'], )]
        
        while garde["pos"][0] in range(length + 1) and garde["pos"][1] in range(width + 1):
            gp = garde['pos']
            dir = garde['dir']
            
            futur = (gp[0] + avance[dir][0], gp[1] + avance[dir][1])
            
            if futur in blocks:
                turn()
            else:
                garde['pos'] = futur
                next = futur + (dir, )
                if not next in visit:
                    visit.append(next)
                else:
                    cpt += 1
                    break

        blocks.remove(newBlock)

print(cpt)