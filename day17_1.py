register = []
program = []

with open("input.txt", "r", encoding="utf-8") as fichier:
    for i in range(3):
        line = fichier.readline().removesuffix('\n').split(':')[1]
        register.append(int(line))
    
    fichier.readline()
    program = [int(x) for x in fichier.readline().removesuffix('\n').split(':')[1].split(',')]

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

print(",".join([str(x) for x in res]))