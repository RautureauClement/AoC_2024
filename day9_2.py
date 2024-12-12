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

blocs.reverse()

for bloc in blocs:
    res.append(bloc)
    for index, empty in enumerate(emptys):
        if empty[0] > bloc[0]:
            break
        if empty[1] >= bloc[1]:
            res.pop()
            res.append((empty[0], bloc[1], bloc[2]))
            emptys.pop(index)
            emptys.insert(index, (empty[0] + bloc[1], empty[1] - bloc[1]))
            break
        
sum = 0
for bloc in res:
    sum += bloc[2] * (bloc[1] * (bloc[0] + bloc[0] + bloc[1] - 1) / 2)

print(sum)