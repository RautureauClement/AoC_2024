nums = []

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        nums = [int(x) for x in line.split(" ")]


def nextGen(nums):
    gen = []
    for num in nums:
        if num == 0:
            gen.append(1)
        elif len(str(num)) % 2 == 0:
            size = len(str(num)) // 2
            gen.append(int(str(num)[:size]))
            gen.append(int(str(num)[size:]))
        else:
            gen.append(num * 2024)
    return gen
    
for i in range(25):
    nums = nextGen(nums)
    
print(len(nums))