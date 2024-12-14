def getAllTuple(x, y, z):
    res = []
    r = range(101)
    for i in r:
        if (z[0] - i * y[0]) % x[0] == 0 and (z[1] - i * y[1]) % x[1] == 0:
            j1 = (z[0] - i * y[0]) // x[0]
            j2 = (z[1] - i * y[1]) // x[1]
            if j1 == j2 and j1 in r:
                res.append((j1, i))
    return res

def getCheapest(list):
    cheapest = list[0][0] * 3 + list[0][1]
    
    for i in range(1, len(list)):
        cheapest = min(cheapest, list[i][0] * 3 + list[i][1])

    return cheapest

sum = 0
with open("input.txt", "r", encoding="utf-8") as fichier:
    A, B, P = None, None, None
    for line in fichier:
        if line == '\n':
            continue
        
        type, values = line.removesuffix('\n').split(':')
        if type == 'Button A':
            A = [int(x.split('+')[1]) for x in values.replace(' ', '').split(',')]
        elif type == 'Button B':
            B = [int(x.split('+')[1]) for x in values.replace(' ', '').split(',')]
        else:
            P = [int(x.split('=')[1]) for x in values.replace(' ', '').split(',')]
            res = getAllTuple(A, B, P)
            if len(res) > 0:
                sum += getCheapest(res)
print(sum)