def getAllTuple(x, y, z):
    res = []
    X = (y[1]*z[0] - y[0]*z[1]) % (x[0]*y[1] - x[1]*y[0])
    Y = (x[0]*z[1] - x[1]*z[0]) % (x[0]*y[1] - x[1]*y[0])
    
    if X != 0 or Y != 0:
        return res
    
    X = (y[1]*z[0] - y[0]*z[1]) // (x[0]*y[1] - x[1]*y[0])
    Y = (x[0]*z[1] - x[1]*z[0]) // (x[0]*y[1] - x[1]*y[0])
    return [(X, Y)]

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
            P = [int(x.split('=')[1]) + 10000000000000 for x in values.replace(' ', '').split(',')]
            res = getAllTuple(A, B, P)
            if len(res) > 0:
                sum += getCheapest(res)
print(sum)