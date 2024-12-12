import random

phase2 = False
before = {}
sum = 0

errs = []

with open("input.txt") as fichier:
    for line in fichier:
        if line == "\n":
            phase2 = True
            continue

        if not phase2:
            num1, num2 = [int(x) for x in line.split("|")]
            if num1 in before.keys():
                before[num1].append(int(num2))
            else:
                before[num1] = [int(num2)]
        else:
            arr = [int(x) for x in line.split(",")]
            arr.reverse()
            size = len(arr)
            err = False
            for i in range(size):
                befores = before.get(arr[i])
                if befores == None or len(befores) == 0:
                    continue
                if err:
                    break

                for j in range(i + 1, size):
                    if arr[j] in befores:
                        err = True
                    if err:
                        break
            
            if err:
                errs.append(arr)
                

i = 0
for arr in errs:
    i += 1
    err = True
    size = len(arr)
    print(f'{i} / {len(errs)} size {len(arr)}')
    while err:
        err = False
        for i in range(size):
            befores = before.get(arr[i])
            if befores == None or len(befores) == 0:
                continue
            if err:
                break

            for j in range(i + 1, size):
                if arr[j] in befores:
                    arr[i], arr[j] = arr[j], arr[i]
                    err = True
                if err:
                    break
    sum += arr[size//2]
                
print(sum)
