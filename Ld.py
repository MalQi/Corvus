def userFlt(prompt):
    print prompt,
    flt = float(raw_input())
    return flt
    
def userStr(prompt):
    print prompt,
    str = raw_input() + " "
    return str
    
def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num

def kmToMi(km):
    return 0.62 * km
