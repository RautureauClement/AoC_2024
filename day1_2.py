left = []
right = []

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        l, r = line.removesuffix('\n').split("   ")
        left.append(int(l))
        right.append(int(r))
        
sum = 0
for i in left:
    sum += right.count(i) * i
    
print(sum)