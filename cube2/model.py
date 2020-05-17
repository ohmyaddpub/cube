#-*coding: UTF-8 -*-

e = ['U0', 'U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']
R = ['U0', 'U1', 'F2', 'U3', 'U4', 'F5', 'U6', 'U7', 'F8', 'D0', 'D1', 'B6', 'D3', 'D4', 'B3', 'D6', 'D7', 'B0', 'L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'R6', 'R3', 'R0', 'R7', 'R4', 'R1', 'R8', 'R5', 'R2', 'F0', 'F1', 'D2', 'F3', 'F4', 'D5', 'F6', 'F7', 'D8', 'U8', 'B1', 'B2', 'U5', 'B4', 'B5', 'U2', 'B7', 'B8']
L = ['B8', 'U1', 'U2', 'B5', 'U4', 'U5', 'B2', 'U7', 'U8', 'F0', 'D1', 'D2', 'F3', 'D4', 'D5', 'F6', 'D7', 'D8', 'L6', 'L3', 'L0', 'L7', 'L4', 'L1', 'L8', 'L5', 'L2', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'U0', 'F1', 'F2', 'U3', 'F4', 'F5', 'U6', 'F7', 'F8', 'B0', 'B1', 'D6', 'B3', 'B4', 'D3', 'B6', 'B7', 'D0']
U = ['U6', 'U3', 'U0', 'U7', 'U4', 'U1', 'U8', 'U5', 'U2', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'F0', 'F1', 'F2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'B0', 'B1', 'B2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R0', 'R1', 'R2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'L0', 'L1', 'L2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']
D = ['U0', 'U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'D6', 'D3', 'D0', 'D7', 'D4', 'D1', 'D8', 'D5', 'D2', 'L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'B6', 'B7', 'B8', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'F6', 'F7', 'F8', 'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'L6', 'L7', 'L8', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'R6', 'R7', 'R8']
F = ['U0', 'U1', 'U2', 'U3', 'U4', 'U5', 'L8', 'L5', 'L2', 'R6', 'R3', 'R0', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'L0', 'L1', 'D0', 'L3', 'L4', 'D1', 'L6', 'L7', 'D2', 'U6', 'R1', 'R2', 'U7', 'R4', 'R5', 'U8', 'R7', 'R8', 'F6', 'F3', 'F0', 'F7', 'F4', 'F1', 'F8', 'F5', 'F2', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8']
B = ['R2', 'R5', 'R8', 'U3', 'U4', 'U5', 'U6', 'U7', 'U8', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'L0', 'L3', 'L6', 'U2', 'L1', 'L2', 'U1', 'L4', 'L5', 'U0', 'L7', 'L8', 'R0', 'R1', 'D8', 'R3', 'R4', 'D7', 'R6', 'R7', 'D6', 'F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'B6', 'B3', 'B0', 'B7', 'B4', 'B1', 'B8', 'B5', 'B2']

facelet2index = {facelet: index for index, facelet in enumerate(e)}
index2facelet = {index: facelet for index, facelet in enumerate(e)}

actions = {"e": e, "R": R, "L": L, "U": U, "D": D, "F": F, "B": B}
actions_compose = {}

def doAct(cube, act):
    return [cube[facelet2index[faceletFrom]] for faceletFrom in act]

def doActs(cube, acts):
    res = cube
    for act in acts:
        res = doAct(res, act)
    return res

def doStrActs(cube, acts):
    return doActs(cube, [actions[i] for i in acts])

def registerActs(acts, name=""):
    if not name:
        name = "".join(acts)
    actions[name] = doStrActs(e, acts)
    actions_compose[name] = "".join(acts)

def difference(cube1, cube2):
    return [c1 == c2 for c1, c2 in zip(cube1, cube2)].count(True)

def differenceU(cube1, cube2):
    return [c1 == c2 for c1, c2 in zip(cube1[:9], cube2[:9])].count(True)

class cube():
    def __init__(self, data):
        self.actionsList = []
        self.data = data

    def doStrActs(self, acts):
        ndata = doStrActs(self.data, acts)
        self.data = ndata
        self.actionsList.append(acts)
    
    def getActs(self):
        return ''.join([i if type(i) is str else ''.join(i) for i in self.actionsList])