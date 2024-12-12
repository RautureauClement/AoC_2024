import re

sum = 0

with open("input.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
    
pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)'
    
occurrences: list[str] = re.findall(pattern, contenu)

do = True

for occurrence in occurrences:
    if occurrence in 'do()':
        do = True
        continue
    if occurrence in 'don\'t()':
        do = False
        continue
    
    if not do:
        continue
    
    a, b = [int(x.replace('mul(', '').replace(')', '')) for x in occurrence.split(",")]
    sum += a*b

print(sum)