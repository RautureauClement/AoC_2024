map = []


with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        map.append(list(line))

map.append([])

xmas = 0

for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] != 'A':
            continue
        
        try:
            word1 = map[row - 1][col - 1] + 'A' + map[row + 1][col + 1]
            word2 = map[row - 1][col + 1] + 'A' + map[row + 1][col - 1]
            
            if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
                xmas += 1
        except:
            pass
            
print(xmas)