p8 = []

for i in range(17):
    p8.append(8 ** i)
    
res = p8[16]

program =  [2, 4, 1, 7, 7, 5, 1, 7, 4, 6, 0, 3, 5, 5, 3, 0]
program2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 5, 3, 0]

for index, i in enumerate(program2):
    res -= i * p8[index]

register = [res - 1, 0, 0]


inc = 0
res = []

def getCombo(opp):
    if opp == 7:
        print("opp 7")
        exit()
    if opp in range(4, 7):
        opp = register[opp % 4]
        
    return opp

def code0(opp, inc):
    opp = getCombo(opp)
    register[0] = register[0] // (2 ** opp)
    return inc + 2

def code1(opp, inc):
    register[1] = register[1] ^ opp
    return inc + 2

def code2(opp, inc):
    opp = getCombo(opp)
    register[1] = opp % 8
    return inc + 2
    
def code3(opp, inc):
    if register[0] != 0:
        return opp
    return inc + 2

def code4(opp, inc):
    register[1] = register[1] ^ register[2]
    return inc + 2
    
def code5(opp, inc):
    opp = getCombo(opp)
    res.append(opp % 8)
    return inc + 2

def code7(opp, inc):
    opp = getCombo(opp)
    register[2] = register[0] // (2 ** opp)
    return inc + 2
    
fun = {
    0: code0,
    1: code1,
    2: code2,
    3: code3,
    4: code4,
    5: code5,
    7: code7
}


while inc < len(program):
    opCode = program[inc]
    opp = program[inc + 1]
    inc = fun[opCode](opp, inc)
    
print(",".join([str(x) for x in program]))
print(",".join([str(x) for x in res]))