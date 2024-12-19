cache = {}
stripes = []

def nbPossible(string):
    if string == '':
        return 1
    if string in cache.keys():
        return cache[string]
    nb = 0
    for stripe in stripes:
        nstr = string.removeprefix(stripe)
        if nstr == string:
            continue
        nb += nbPossible(nstr)
    cache[string] = nb
    return nb

cpt = 0
with open("input.txt", "r", encoding="utf-8") as fichier:
    stripes = fichier.readline().removesuffix('\n').split(', ')
    fichier.readline()
    for line in fichier:
        cpt += nbPossible(line.removesuffix('\n'))

print(cpt)