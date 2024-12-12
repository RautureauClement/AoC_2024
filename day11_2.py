import time

nums = {}

with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        for x in line.split(" "):
            nums[int(x)] = 1

        
def addX(dic, x, add):
    if not x in dic.keys():
        dic[x] = add
    else:
        dic[x] += add
    
    return dic

def nextGen(nums):
    gen = {}
    for num, repeat in nums.items():
        if num == 0:
            gen = addX(gen, 1, repeat)
        elif len(str(num)) % 2 == 0:
            size = len(str(num)) // 2
            
            gen = addX(gen, int(str(num)[:size]), repeat)
            gen = addX(gen, int(str(num)[size:]), repeat)
        else:
            gen = addX(gen, num * 2024, repeat)
    return gen

t = time.time()
    
for i in range(75):
    nums = nextGen(nums)

sum = 0
for i in nums.values():
    sum += i

print(time.time() - t)
print(sum)