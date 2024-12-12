blocs = []
emptys = []

with open('input.txt') as fichier:
    pos = 0
    for l in fichier:
        for index, num in enumerate(l):
            if index % 2 == 0:
                blocs.append((pos, int(num), index // 2))
            else:
                emptys.append((pos, int(num)))
            
            pos += int(num)
    
res = []
while len(blocs) > 0:
    bloc = blocs.pop(0)
    empty = emptys.pop(0)
    
    if bloc[0] < empty[0]:
        res.append(bloc)
        emptys.insert(0, empty)
        continue
    
    
    if len(blocs) == 0:
        res.append((empty[0], bloc[1], bloc[2]))
        break
    
    last = blocs.pop()
    blocs.insert(0, bloc)
    
    if last[1] > empty[1]:
        res.append((empty[0], empty[1], last[2]))
        blocs.append((last[0], last[1] - empty[1], last[2]))
    else:
        emptys.insert(0, (empty[0] + last[1], empty[1] - last[1]))
        res.append((empty[0], last[1], last[2]))

sum = 0
for bloc in res:
    sum += bloc[2] * (bloc[1] * (bloc[0] + bloc[0] + bloc[1] - 1) / 2)
    
print(sum)