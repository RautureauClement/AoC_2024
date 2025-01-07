def isPossible(strs, stripes):
    if len(strs.replace('.', '')) == 0:
        return True
    
    for str in strs.split("."):
        if str == '': continue
        oneStripe = False
        for stripe in stripes:
            if stripe in str:
                oneStripe = isPossible(str.replace(stripe, '.', 1), stripes)
                if oneStripe: break
        
        if not oneStripe:
            return False
        
    return True

def delStripes(stripes):
    rm = []
    for stripe in stripes:
        subStripes = stripes.copy()
        subStripes.remove(stripe)
        if isPossible(stripe, subStripes):
            rm.append(stripe)
    
    return sorted([x for x in stripes if not x in rm], key=len, reverse=True)
    

cpt = 0
with open("input.txt", "r", encoding="utf-8") as fichier:
    stripes = fichier.readline().removesuffix('\n').split(', ')
    fichier.readline()
    stripes = delStripes(stripes)
    
    for line in fichier:
        print(line)
        cpt += 1 if isPossible(line.removesuffix('\n'), stripes) else 0

print(cpt)