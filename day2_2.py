goodLine = 0

def isGoodLine(nbs):
    inc = None
    for i in range(len(nbs) - 1):
        diff = nbs[i] - nbs[i + 1]
        if diff != 0 and inc == None:
            inc = diff / abs(diff)
        
        if diff == 0 or diff / abs(diff) != inc or abs(diff) > 3:
            return False
    return True

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        nbs = [int(x) for x in line.split(" ")]
        isGood = isGoodLine(nbs)
        for i in range(len(nbs)):
            nbs2 = nbs[:i] + nbs[i + 1:]
            isGood |= isGoodLine(nbs2)
            if isGood:
                goodLine += 1
                break
            
print(goodLine)