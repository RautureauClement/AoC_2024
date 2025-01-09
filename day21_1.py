class Pad:
    def __init__(self, pad, pos):
        self.pad = pad
        self.pos = pos
        
    def move(self, move):
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        
    def getCode(self, code):
        path = []
        for c in code:
            if self.pad[c] == self.pos:
                path.append('A')
                continue
            if self.pos[0] == self.pad[c][0] or self.pos[1] == self.pad[c][1]:
                coeff = 0
            else:
                coeff = (self.pos[1] - self.pad[c][1]) / (self.pos[0] - self.pad[c][0])
            if coeff >= 0:
                if (self.pos[0], self.pad[c][1]) in self.pad.values():
                    for _ in range(abs(self.pad[c][1] - self.pos[1])):
                        path.append('>' if self.pad[c][1] > self.pos[1] else '<')
                    for _ in range(abs(self.pad[c][0] - self.pos[0])):
                        path.append('v' if self.pad[c][0] > self.pos[0] else '^')
                else:
                    for _ in range(abs(self.pad[c][0] - self.pos[0])):
                        path.append('v' if self.pad[c][0] > self.pos[0] else '^')
                    for _ in range(abs(self.pad[c][1] - self.pos[1])):
                        path.append('>' if self.pad[c][1] > self.pos[1] else '<')
            else:
                
                if (self.pad[c][0], self.pos[1]) in self.pad.values():
                    for _ in range(abs(self.pad[c][0] - self.pos[0])):
                        path.append('v' if self.pad[c][0] > self.pos[0] else '^')
                    for _ in range(abs(self.pad[c][1] - self.pos[1])):
                        path.append('>' if self.pad[c][1] > self.pos[1] else '<')
                else:
                    for _ in range(abs(self.pad[c][1] - self.pos[1])):
                        path.append('>' if self.pad[c][1] > self.pos[1] else '<')
                    for _ in range(abs(self.pad[c][0] - self.pos[0])):
                        path.append('v' if self.pad[c][0] > self.pos[0] else '^')
            path.append('A')
            self.pos = self.pad[c]
        return "".join(path)
                

sum = 0
with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        pad = Pad({
            '7': (0, 0),
            '8': (0, 1),
            '9': (0, 2),
            '4': (1, 0),
            '5': (1, 1),
            '6': (1, 2),
            '1': (2, 0),
            '2': (2, 1),
            '3': (2, 2),
            '0': (3, 1),
            'A': (3, 2)
        }, (3, 2))
        
        bot1 = Pad({
            '^': (0, 1),
            'A': (0, 2),
            '<': (1, 0),
            'v': (1, 1),
            '>': (1, 2),
        }, (0, 2))
        bot2 = Pad({
            '^': (0, 1),
            'A': (0, 2),
            '<': (1, 0),
            'v': (1, 1),
            '>': (1, 2),
        }, (0, 2))
        
        code = line.removesuffix('\n')
        path = bot2.getCode(bot1.getCode(pad.getCode(code)))
        # print("".join(path))
        
        sum += int(code.removesuffix('A')) * len(path)
        
print(sum)

# 161472 to high