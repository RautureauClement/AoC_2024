def getNext(secret):
    secret ^= secret * 64
    secret %= 16777216
    secret ^= secret // 32
    secret %= 16777216
    secret ^= secret * 2048
    secret %= 16777216
    return secret

cache = []
cacheChange = []
with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        secret = int(line.removesuffix('\n'))
        lastNum = []
        for _ in range(10):
            lastNum.append(int(str(secret)[-1]))
            secret = getNext(secret)
        lastNum.append(int(str(secret)[-1]))
        cache.append(lastNum)
        change = ""
        val = lastNum[0]
        for num in lastNum:
            change += str(num - val) + ","
            val = num
        cacheChange.append(change)

maxi = 0
size = len(cache)

print(cache)
print(cacheChange)
for a in range(-5, 6):
    print(a)
    for b in range(-5, 6):
        for c in range(-5, 6):
            for d in range(-5, 6):
                change = ','.join(str(x) for x in [a, b, c, d])
                sum = 0
                nums = []
                for i, line in enumerate(cacheChange):
                    index = line.find(change)
                    if index > -1:
                        index = line[:index+1].count(",")
                        res = cache[i][index + 3]
                        sum += res
                        nums.append(res)
                        
                    if sum + (size - i) * 9 < maxi:
                        break
                maxi = max(maxi, sum)
                if maxi == sum:
                    bNums = nums
                    bChanges = change

print(maxi)
print(bNums)
print(bChanges)
#2572 to high