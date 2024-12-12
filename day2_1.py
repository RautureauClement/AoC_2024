goodLine = 0

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        nbs = [int(x) for x in line.split(" ")]
        inc = None
        isGood = True
        for i in range(len(nbs) - 1):
            diff = nbs[i] - nbs[i + 1]
            if diff != 0 and inc == None:
                inc = diff / abs(diff)
            
            if diff == 0 or diff / abs(diff) != inc or abs(diff) > 3:
                isGood = False
                break
        
        if isGood:
            goodLine += 1
            
print(goodLine)