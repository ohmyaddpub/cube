import utils
import random
import itertools
from model import *
from collections import Counter

class cube():
    def __init__(self, data):
        self.actionsList = []
        self.data = data

    def doStrActs(self, acts):
        ndata = doStrActs(self.data, acts)
        self.data = ndata
        self.actionsList.append(acts)
        a = calc(self)
        print(a[1], a[2], a[3])
    
    def getActs(self):
        return ''.join([i if type(i) is str else ''.join(i) for i in self.actionsList])

dacts = {'R0': 'lUL', 'L2': 'luL', 'F0': 'FUf', 'B2': 'Fuf', 'B0': 'UlUL', 'F2': 'UluL', 'L0': 'uFUf', 'R2': 'uFuf', 'F6': 'lULFUf', 'U2': 'luLFUf', 'U6': 'lfLLFL', 'U8': 'lflFuL', 'L8': 'FufluL', 'U0': 'FLFlUf'}
for k, v in dacts.copy().items():
    dacts[facelet2index[k]] = v

uacts = {'R8': 'lDL', 'L6': 'ldL', 'B8': 'BDb', 'F6': 'Bdb', 'F8': 'DlDL', 'B6': 'DldL', 'L8': 'dBDb', 'R6': 'dBdb', 'B2': 'lDLBDb', 'D2': 'ldLBDb', 'D6': 'lfDDFL', 'D8': 'lfdFdL', 'L0': 'BdbldL', 'D0': 'BLBlDb'}
for k, v in uacts.copy().items():
    uacts[facelet2index[k]] = v

u2edges = {'L3': 'URuDb', 'R7': 'UruDB', 'L7': 'uLUdb', 'R5': 'ulUdB', 'B7': 'BUdru', 'F3': 'BuDlU', 'F5': 'bUdRu', 'F7': 'UDruDB', 'D7': 'LrBBlR', 'B3': 'UUFuDru', 'B5': 'UUfUdLU', 'L5': 'UrUdFUU', 'R3': 'uLuDfUU', 'D5': 'DLrBBlR', 'D3': 'dLrBBlR', 'D1': 'URfrFruB'}
for k, v in u2edges.copy().items():
    u2edges[facelet2index[k]] = v


def egen(frm, to):
    r1 = u2edges[frm]
    if to == "U3" or to == "L1":
        r2 = "U"
        r4 = "u"
    elif to == "U5" or to == "R1":
        r2 = "u"
        r4 = "U"
    elif to == 'U7' or to == "F1":
        r2 = 'UU'
        r4 = "UU"
    elif to == 'U1' or to == "B1":
        r2 = 'U'
        r4 = "u"
    else:
        raise(Exception('to is err'))
    r3 = ''.join([i.lower() if i.isupper() else i.upper() for i in r1[::-1]])
    return ''.join([r1, r2, r3, r4])


def dgen(frm, to):
    r1 = dacts[frm]
    if to == "D6":
        r2 = "D"
        r4 = "d"
    elif to == "D2":
        r2 = "d"
        r4 = "D"
    elif to == 'D8':
        r2 = 'DD'
        r4 = "DD"
    else:
        raise(Exception('to is err'))
    r3 = ''.join([i.lower() if i.isupper() else i.upper() for i in r1[::-1]])
    return ''.join([r1, r2, r3, r4])

def ugen(frm, to):
    r1 = uacts[frm]
    if to == "U6":
        r2 = "U"
        r4 = "u"
    elif to == "U2":
        r2 = "u"
        r4 = "U"
    elif to == 'U8':
        r2 = 'UU'
        r4 = "UU"
    else:
        raise(Exception('to is err'))
    r3 = ''.join([i.lower() if i.isupper() else i.upper() for i in r1[::-1]])
    return ''.join([r1, r2, r3, r4])



def phase1(cube):
    ufaces = [facelet2index[i] for i in ["R0", "R1", "R2", "L0", "L1", "L2", "F0", "F1", "F2", "B0", "B1", "B2", "U0", "U2", "U6", "U8"]]
    dfaces = [facelet2index[i] for i in ["R6", "R7", "R8", "L6", "L7", "L8", "F6", "F7", "F8", "B6", "B7", "B8", "D0", "D2", "D6", "D8"]]

    for corner in ["U6", "U8", "D6", "D8"]:
        whereis = cube.data.index(facelet2index[corner])
        place = ufaces if facelet2index[corner] in ufaces else dfaces
        if whereis in place:
            if place == ufaces:
                cube.doStrActs(dgen(whereis, "D2"))
            else:
                cube.doStrActs(ugen(whereis, "U2"))

        whereis = cube.data.index(facelet2index[corner])
        if place == ufaces:
            cube.doStrActs(ugen(whereis, corner))
            cube.doStrActs(ugen(whereis, corner))
        else:
            cube.doStrActs(dgen(whereis, corner))
            cube.doStrActs(dgen(whereis, corner))
    
    """
    fourcorners = [facelet2index[i] for i in ["U0", "U2", "D0", "D2"]]
    for corner in ["U0", "D0"]:
        whereis = cube.data.index(facelet2index[corner])
        while whereis not in fourcorners:
            if whereis in ufaces:
                cube.doStrActs(ugen(whereis, "U2"))
            else:
                cube.doStrActs(dgen(whereis, "D2"))
            whereis = cube.data.index(facelet2index[corner])
    """


def phase11(cube):
    ufaces = [facelet2index[i] for i in ["R0", "R1", "R2", "L0", "L1", "L2", "F0", "F1", "F2", "B0", "B1", "B2", "U0", "U2", "U6", "U8"]]
    dfaces = [facelet2index[i] for i in ["R6", "R7", "R8", "L6", "L7", "L8", "F6", "F7", "F8", "B6", "B7", "B8", "D0", "D2", "D6", "D8"]]
    corners = {"U0": ("U0", "L0", "B2"),
               "U2": ("U2", "B0", "R2"),
               "U6": ("U6", "F0", "L2"),
               "U8": ("U8", "R0", "F2"),
               "D0": ("D0", "L8", "F6"),
               "D2": ("D2", "F8", "R6"),
               "D6": ("D6", "B8", "L6"),
               "D8": ("D8", "R8", "B6")}
    corners2 = {v2: k for k, v in corners.items() for v2 in v}
    
    nowfaces = [index2facelet[cube.data.index(facelet2index[i])] for i in ["U0", "U2", "U6", "U8", "D0", "D2", "D6", "D8"]]
    for face in nowfaces[:4]:
        lcube = corners2[face]


    for face in nowfaces[4:8]:
        lcube = corners2[face]
    



def phase2(cube):
    topedges = [facelet2index[i] for i in ["U3", "U5", "U7", "F1", "L1", "R1", "U1", "B1"]]
    topedges2 = [facelet2index[i] for i in ["U1", "B1"]]
    for edge in ["U3", "U7"]:
        whereisedge = cube.data.index(facelet2index[edge])
        if whereisedge in topedges2:
            cube.doStrActs(egen("D7", index2facelet[whereisedge]))
        if whereisedge in topedges:
            cube.doStrActs(egen("D7", index2facelet[whereisedge]))
        whereisedge = cube.data.index(facelet2index[edge])
        cube.doStrActs(egen(whereisedge, edge))
        cube.doStrActs(egen(whereisedge, edge))
    
    for edge in ["F3", "F5", "B3", "B5", "D1", "D3", "D5", "D7"]:
        whereisedge = cube.data.index(facelet2index[edge])
        if whereisedge in topedges2:
            cube.doStrActs(egen("D7", index2facelet[whereisedge]))
        if whereisedge in topedges:
            cube.doStrActs(egen("D7", index2facelet[whereisedge]))
        whereisedge = cube.data.index(facelet2index[edge])
        cube.doStrActs(egen(whereisedge, "U5"))
        cube.doStrActs(egen(whereisedge, "U5"))
        cube.doStrActs(egen(facelet2index[edge], "U5"))


def calc(cube):
    ths = {"U0": 1, "L0": 2, "B2": 3,
           "U2": 1, "B0": 2, "R2": 3,
           "U6": 1, "F0": 2, "L2": 3,
           "U8": 1, "R0": 2, "F2": 3,
           "D0": 1, "L8": 2, "F6": 3,
           "D2": 1, "F8": 2, "R6": 3,
           "D6": 1, "B8": 2, "L6": 3,
           "D8": 1, "R8": 2, "B6": 3}
    thss = []
    faces = [facelet2index[i] for i in ["U0", "U2", "U6", "U8", "D0", "D2", "D6", "D8"]]
    for i in faces:
        thss.append(ths[index2facelet[cube.data[i]]])
    return Counter(thss)


def phase10(cube):
    ufaces = [facelet2index[i] for i in ["R0", "R1", "R2", "L0", "L1", "L2", "F0", "F1", "F2", "B0", "B1", "B2", "U0", "U2", "U6", "U8"]]
    dfaces = [facelet2index[i] for i in ["R6", "R7", "R8", "L6", "L7", "L8", "F6", "F7", "F8", "B6", "B7", "B8", "D0", "D2", "D6", "D8"]]

    # D0 To UP
    whereisD0 = cube.data.index(facelet2index["D0"])
    if whereisD0 in ufaces:
        cube.doStrActs(dgen(whereisD0, "D2"))

    whereisD0 = cube.data.index(facelet2index["D0"])
    cube.doStrActs(ugen(whereisD0, "U8"))
    cube.doStrActs(ugen(whereisD0, "U8"))

    # D2 To UP
    whereisD2 = cube.data.index(facelet2index["D2"])
    if whereisD2 in ufaces:
        cube.doStrActs(dgen(whereisD2, "D2"))

    whereisD2 = cube.data.index(facelet2index["D2"])
    cube.doStrActs(ugen(whereisD2, "U6"))
    cube.doStrActs(ugen(whereisD2, "U6"))

    # U0 to Down
    whereisU0 = cube.data.index(facelet2index["U0"])
    if whereisU0 in dfaces:
        cube.doStrActs(ugen(whereisU0, "U2"))

    whereisU0 = cube.data.index(facelet2index["U0"])
    cube.doStrActs(dgen(whereisU0, "D8"))
    cube.doStrActs(dgen(whereisU0, "D8"))

    # U2 To Down
    whereisU2 = cube.data.index(facelet2index["U2"])
    if whereisU2 in dfaces:
        cube.doStrActs(ugen(whereisU2, "U2"))

    whereisU2 = cube.data.index(facelet2index["U2"])
    cube.doStrActs(dgen(whereisU2, "D6"))
    cube.doStrActs(dgen(whereisU2, "D6"))

    # D6 To UP
    whereisD6 = cube.data.index(facelet2index["D6"])
    if whereisD6 in ufaces:
        cube.doStrActs(dgen(whereisD6, "D2"))

    whereisD6 = cube.data.index(facelet2index["D6"])
    cube.doStrActs(ugen(whereisD6, "U2"))

    # D8 To UP
    whereisD8 = cube.data.index(facelet2index["D8"])
    if whereisD8 in ufaces:
        cube.doStrActs(dgen(whereisD8, "D2"))

    whereisD8 = cube.data.index(facelet2index["D8"])
    cube.doStrActs(ugen(whereisD8, "U2"))

    # turn back
    cube.doStrActs("BBFF")

    """
    while cube.data.index(facelet2index["U6"]) != facelet2index["U6"]:
        cube.doStrActs("U")
        cube.doStrActs(ugen("L0", "U6"))
        cube.doStrActs("u")
    """


if __name__ == '__main__':
    cases = ["llfRBUudfbdulDUbRRdL",
            "ddbBuulBdlrdLflRUubb",
            "ruDufDrFlFUfbbduBFU",
            "UUFublFLuLlrlrlfRrd"]
    case = ''.join([random.choice('UuDdLlRrFfBb') for i in range(26)])
    #case = cases[3]

    """
    res = set()
    for i in range(1000):
        case = ''.join([random.choice('UuDdLlRrFfBb') for i in range(random.randint(2, 30))])
        c = cube(e)
        c.doStrActs(case)
        a = calc(c)
        res.add((a[1], a[2], a[3]))
    print(res)

    #for act in itertools.product("UuDdLlRrFfBb", repeat=2):
    #for act in [ugen("R8", "U2"), ugen("L8", "U8"), ugen("L0", "U2"), ugen("B2", "U2")]:
    c = cube(e)
    for act in [ugen("D0", "U8")] * 6:
        c.doStrActs(act)
        a = calc(c)
        print(''.join(act), (a[1], a[2], a[3]))
    """



    c = cube(e)
    c.doStrActs(case)
    c.actionsList = []

    print("depose")
    phase10(c)
    print(case)
    print(c.getActs())
    print([c.data[facelet2index[i]] == facelet2index[i] for i in ["U0", "U2", "U6", "U8", "D0", "D2", "D6", "D8"]].count(False))

    #c = cube(e)
    #c.doStrActs(case)
    #c.actionsList = []
    #phase2(c)
    #print(c.getActs())
