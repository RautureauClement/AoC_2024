map = []


with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        map.append(list(line))

map.append([])
        
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]
xmas = 0

for row in range(len(map)):
    for col in range(len(map[row])):
        for direction in directions:
            str = ""
            try:
                for cpt in range(4):
                    str += map[row + cpt * direction[0]][col + cpt * direction[1]]
                if str == "XMAS":
                    xmas += 1
            except:
                pass
            
print(xmas)