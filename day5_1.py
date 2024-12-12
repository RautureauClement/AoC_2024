phase2 = False
before = {}
sum = 0

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
            
            if not err:
                sum += arr[size//2]
                
print(sum)
