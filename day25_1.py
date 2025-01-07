keys = []
serrures = []

with open("input.txt", "r", encoding="utf-8") as fichier:
    fit = [0, 0, 0, 0, 0]
    key = None
    for line in fichier:
        line = line.removesuffix('\n')
        if line in "":
            if key:
                keys.append(fit)
            else:
                serrures.append(fit)
            fit = [0, 0, 0, 0, 0]
            key = None
            continue
        if key == None:
            key = (line == "#####")
        for index, char in enumerate(line):
            if char == '#':
                fit[index] += 1
                
    if key:
        keys.append(fit)
    else:
        serrures.append(fit)
    fit = [0, 0, 0, 0, 0]
    
    
cpt = 0
for key in keys:
    for serrure in serrures:
        done = True
        for i in range(5):
            if key[i] + serrure[i] > 7:
                done = False
                break
        if done:
            cpt += 1
print(cpt)