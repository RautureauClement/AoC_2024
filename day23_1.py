
pc = {}

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        conn = line.removesuffix('\n').split('-')
        for index, con in enumerate(conn):
            if con not in pc.keys():
                pc[con] = []
            pc[con].append(conn[(index+1) % 2])


set = []
for ordi in pc.keys():
    if not ordi.startswith('t'):
        continue
    
    for conn in pc[ordi]:
        if conn == ordi:
            continue
        for con in pc[conn]:
            if conn == ordi:
                continue
            for last in pc[con]:
                if last == ordi:
                    key = [ordi, conn, con]
                    key.sort()
                    if key not in set:
                        set.append(key)
                    
print(len(set))