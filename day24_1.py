cache = {}

with open("input.txt", "r", encoding="utf-8") as fichier:
    init = True
    for line in fichier:
        line = line.removesuffix('\n')
        if line in "":
            init = False
            continue
        
        if init:
            sp = line.split(":")
            cache[sp[0]] = int(sp[1])
        else:
            sp = line.split(' -> ')
            cache[sp[1]] = sp[0]

def evaluate(name):
    value = cache[name]
    if isinstance(value, str):
        sp = value.split(' ')
        val1 = evaluate(sp[0])
        val2 = evaluate(sp[2])
        
        if sp[1] == 'OR':
            value = 1 if val1 == 1 or val2 == 1 else 0
        elif sp[1] == 'XOR':
            value = 1 if val1 != val2 else 0
        elif sp[1] == 'AND':
            value = 1 if val1 == 1 and val2 == 1 else 0
        
        cache[name] = value
    return value

out = ""
for key in sorted(cache.keys()):
    evaluate(key)
    if key.startswith('z'):
        out += str(cache[key])

print(int(out[::-1], 2))