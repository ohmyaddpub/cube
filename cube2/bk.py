import utils
import random
from model import *


class cube():
    def __init__(self, data):
        self.actionsList = []
        self.data = data

    def doStrActs(self, acts):
        ndata = doStrActs(self.data, acts)
        # if self.data[facelet2index["L3"]] != ndata[facelet2index["L3"]]:
        #    print("!!!!!!!!edge change!", acts)
        self.data = ndata
        self.actionsList.append(acts)
    
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

    for corner in ["U0", "U2", "D0", "D2"]:
        whereis = cube.data.index(facelet2index[corner])
        if whereis in ufaces:
            cube.doStrActs(dgen(whereis, "D2"))
        else:
            cube.doStrActs(ugen(whereis, "U2"))
        

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



if __name__ == '__main__':
    cases = ["llfRBUudfbdulDUbRRdL",
            "ddbBuulBdlrdLflRUubb",
            "ruDufDrFlFUfbbduBFU"]
    case = ''.join([random.choice('UuDdLlRrFfBb') for i in range(20)])
    case = cases[2]

    c = cube(e)
    c.doStrActs(case)
    c.actionsList = []

    phase1(c)
    print(case)
    print(c.getActs())

    #c = cube(e)
    #c.doStrActs(case)
    #c.actionsList = []
    #phase2(c)
    #print(c.getActs())
