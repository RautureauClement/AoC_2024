length = 0
width = 0

antenne = {}

with open('input.txt') as fichier:
    for line in fichier:
        for index, char in enumerate(line):
            if char != '.' and char != '\n':
                antenne.setdefault(char, []).append((length, index))
            width = max(width, index)
        length += 1

antinoeud = []

for frequence in antenne:
    for index, pos in enumerate(antenne[frequence]):
        for oPos in antenne[frequence][index + 1:]:
            dif = (oPos[0] - pos[0], oPos[1] - pos[1])
            aNp = (pos[0] - dif[0], pos[1] - dif[1])
            aNn = (oPos[0] + dif[0], oPos[1] + dif[1])
            
            if aNp[0] in range(length) and aNp[1] in range(width) and not aNp in antinoeud:
                antinoeud.append(aNp)
            
            if aNn[0] in range(length) and aNn[1] in range(width) and not aNn in antinoeud:
                antinoeud.append(aNn)
                
print(len(antinoeud))