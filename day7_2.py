
def rec(init: int, res: int, other: list[int]):
    if len(other) == 0:
        return init == res
    
    next = other.pop(0)
    return rec(init + next, res, other.copy()) or rec(init * next, res, other.copy()) or rec(int(str(init) + str(next)), res, other.copy())

cpt = 0

with open('input.txt') as fichier:
  for line in fichier:
    res, nums = line.split(':')
    res = int(res)
    nums = [int(x) for x in nums.split(' ') if x != '']
    init = nums.pop(0)
    if rec(init, res, nums):
        cpt += res
print(cpt)