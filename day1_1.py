left = []
right = []

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        l, r = line.removesuffix('\n').split("   ")
        left.append(int(l))
        right.append(int(r))
        
left.sort()
right.sort()

sum = 0
for i in range(len(left)):
    sum += abs(left[i] - right[i])
    
print(sum)