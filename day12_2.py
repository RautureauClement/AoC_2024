garden = []
heigth = None
width = None

class Region:
    cases: list
    char: str
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def __init__(self, char, pos):
        self.char = char
        self.cases = []
        self.cases.append(pos)
            
    def extend(self, pos):
        for dir in self.dirs:
            next = (pos[0] + dir[0], pos[1] + dir[1])
            if not next[0] in heigth or not next[1] in width:
                continue

            if garden[next[0]][next[1]] == self.char:
                garden[next[0]][next[1]] = '.'
                self.cases.append(next)
                self.extend(next)
    
    def getValue(self):
        area = len(self.cases)
        perimeter = 4 * area
        for index, case in enumerate(self.cases):
            for indexDir, dir in enumerate(self.dirs):
                if (case[0] + dir[0], case[1] + dir[1]) in self.cases[index:]:
                    perimeter -= 2
                    for vertical in range((indexDir + 1) % 2, len(self.dirs), 2):
                        if not (case[0] + dir[0] + self.dirs[vertical][0], case[1] + dir[1] + self.dirs[vertical][1]) in self.cases and not (case[0] + self.dirs[vertical][0], case[1] + self.dirs[vertical][1]) in self.cases:
                            perimeter -= 1
        return area * perimeter


regions = {}

with open('input.txt') as fichier:
    for line in fichier:
        garden.append(list(line.removesuffix('\n')))
        
heigth = range(len(garden))
width = range(len(garden[0]))

for i in heigth:
    for j in width:
        char = garden[i][j]
        if char == '.':
            continue
        
        regions.setdefault(char, [])
        
        char, garden[i][j] = garden[i][j], '.'
        
        region = Region(char, (i, j))
        region.extend((i, j))
        
        regions[char].append(region)
        
sum = 0
for region in regions.values():
    for reg in region:
        sum += reg.getValue()
    
print(sum)