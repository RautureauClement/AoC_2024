def getNext(secret):
    secret ^= secret * 64
    secret %= 16777216
    secret ^= secret // 32
    secret %= 16777216
    secret ^= secret * 2048
    secret %= 16777216
    return secret

sum = 0
with open("input.txt", "r", encoding="utf-8") as fichier:
    for line in fichier:
        secret = int(line.removesuffix('\n'))
        for _ in range(2000):
            secret = getNext(secret)
            
        sum += secret
print(sum)
        
