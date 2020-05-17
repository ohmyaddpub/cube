import utils
import random
import itertools
from model import *
from collections import Counter

class cube():
    def __init__(self, data):
        self.actionsList = []
        self.actionsList2 = []
        self.data = data

    def doStrAct(self, act, verbose=True):
        toprint = actions_compose[act] if act in actions_compose else act
        self.actionsList.append(toprint)
        self.actionsList2.append(act)

        ndata = doStrActs(self.data, (act,))
        self.data = ndata

    def getActs(self):
        return ''.join([i if type(i) is str else ''.join(i) for i in self.actionsList])


def corner_face_perm(cube):
    faces = [e[i * 9 + j] for i in range(6) for j in [0, 2, 6, 8]]
    move = {face: index2facelet[cube.data.index(face)] for face in faces}

    done = set()
    res = []
    for face in move:
        if face in done:
            continue
        nxt = move[face]
        nres = [nxt]
        done.add(face)
        done.add(nxt)
        while nxt != face:
            nxt = move[nxt]
            nres.append(nxt)
            done.add(nxt)
        res.append(nres)

    count = 0
    for i in res:
        length = len(i)
        if length > 1:
            count += (length - 1)
    return count


def corner_cube_perm(cube):
    corners = {"U0": ("U0", "L0", "B2"),
               "U2": ("U2", "B0", "R2"),
               "U6": ("U6", "F0", "L2"),
               "U8": ("U8", "R0", "F2"),
               "D0": ("D0", "L8", "F6"),
               "D2": ("D2", "F8", "R6"),
               "D6": ("D6", "B8", "L6"),
               "D8": ("D8", "R8", "B6")}
    corners2 = {v2: k for k, v in corners.items() for v2 in v}

    move = {cor: corners2[index2facelet[cube.data.index(cor)]] for cor in corners.keys()}

    done = set()
    res = []
    for cor in move:
        if cor in done:
            continue
        nxt = move[cor]
        nres = [nxt]
        done.add(cor)
        done.add(nxt)
        while nxt != cor:
            nxt = move[nxt]
            nres.append(nxt)
            done.add(nxt)
        res.append(nres)

    count = 0
    for i in res:
        length = len(i)
        if length > 1:
            count += (length - 1)
    return count


def edge_face_perm(cube):
    faces = [e[i * 9 + j] for i in range(6) for j in [1, 3, 5, 7]]
    move = {face: index2facelet[cube.data.index(face)] for face in faces}

    done = set()
    res = []
    for face in move:
        if face in done:
            continue
        nxt = move[face]
        nres = [nxt]
        done.add(face)
        done.add(nxt)
        while nxt != face:
            nxt = move[nxt]
            nres.append(nxt)
            done.add(nxt)
        res.append(nres)

    count = 0
    for i in res:
        length = len(i)
        if length > 1:
            count += (length - 1)
    return count


def edge_cube_perm(cube):
    corners = {"U1": ("U1", "B1"),
               "U3": ("U3", "L1"),
               "U5": ("U5", "R1"),
               "U7": ("U7", "F1"),
               "D1": ("D1", "F7"),
               "D3": ("D3", "L7"),
               "D5": ("D5", "R7"),
               "D7": ("D7", "B7"),
               "L3": ("L3", "B5"),
               "L5": ("L5", "F3"),
               "R3": ("R3", "F5"),
               "R5": ("R5", "B3"),
               }
    corners2 = {v2: k for k, v in corners.items() for v2 in v}

    move = {cor: corners2[index2facelet[cube.data.index(cor)]] for cor in corners.keys()}

    done = set()
    res = []
    for cor in move:
        if cor in done:
            continue
        nxt = move[cor]
        nres = [nxt]
        done.add(cor)
        done.add(nxt)
        while nxt != cor:
            nxt = move[nxt]
            nres.append(nxt)
            done.add(nxt)
        res.append(nres)

    count = 0
    for i in res:
        length = len(i)
        if length > 1:
            count += (length - 1)
    return count

def edge_face_count(cube):
    redges = ["U1", "U3", "U5", "U7", "D1", "D3", "D5", "D7", "L3", "L5", "R3", "R5"]
    rindex = [facelet2index[i] for i in redges]
    return [].count(True)


def phase1(cube):
    ufaces = ["R0", "R1", "R2", "L0", "L1", "L2", "F0", "F1", "F2", "B0", "B1", "B2", "U0", "U2", "U6", "U8"]
    dfaces = ["R6", "R7", "R8", "L6", "L7", "L8", "F6", "F7", "F8", "B6", "B7", "B8", "D0", "D2", "D6", "D8"]
    fourcorners = ["U0", "U2", "D0", "D2"]

    if corner_cube_perm(c) % 2 != 0:
        cube.doStrAct("L")

    for corner in ["U6", "U8"]:
        whereis = index2facelet[cube.data.index(corner)]
        if whereis in ufaces:
            cube.doStrAct("D0" + "D2" + whereis)

        whereis = index2facelet[cube.data.index(corner)]
        cube.doStrAct("U0" + corner + whereis)
        cube.doStrAct("U0" + corner + whereis)

    for corner in ["D6", "D8"]:
        whereis = index2facelet[cube.data.index(corner)]
        if whereis in dfaces:
            cube.doStrAct("U0" + "U2" + whereis)

        whereis = index2facelet[cube.data.index(corner)]
        cube.doStrAct("D0" + corner + whereis)
        cube.doStrAct("D0" + corner + whereis)

    for corner in ["U2", "U0"]:
        whereis = index2facelet[cube.data.index(corner)]
        if whereis in ufaces:
            cube.doStrAct("D0" + "D2" + whereis)

        whereis = index2facelet[cube.data.index(corner)]
        cube.doStrAct("U0" + "U2" + whereis)
    
    for i in range(3):
        nowis = cube.data[facelet2index["D0"]]
        if nowis in fourcorners:
            break
        cube.doStrAct("D0" + "D2" + "F6")


def phase2(cube):
    uedges = ["U3", "U5", "U7", "F1", "L1", "R1", "U1", "B1"]
    dedges = ["D1", "D3", "D5", "D7", "F7", "L7", "R7", "B7"]
    twoedges = ["U1", "U5"]

    for edge in ["U3", "U7"]:
        whereisedge = index2facelet[cube.data.index(edge)]
        if whereisedge in uedges:
            cube.doStrAct("D1" + "D5" + whereisedge)
        whereisedge = index2facelet[cube.data.index(edge)]
        cube.doStrAct("U1" + edge + whereisedge)
        cube.doStrAct("U1" + edge + whereisedge)

    for edge in ["D3", "D7"]:
        whereisedge = index2facelet[cube.data.index(edge)]
        if whereisedge in dedges:
            cube.doStrAct("U1" + "U5" + whereisedge)
        whereisedge = index2facelet[cube.data.index(edge)]
        cube.doStrAct("D1" + edge + whereisedge)
        cube.doStrAct("D1" + edge + whereisedge)
    
    for edge in ["F3", "F5", "B3", "B5"]:
        whereisedge = index2facelet[cube.data.index(edge)]
        if whereisedge in uedges:
            cube.doStrAct("D1" + "D5" + whereisedge)
            cube.doStrAct("D1" + "D5" + whereisedge)
            cube.doStrAct("D1" + "D5" + edge)
        else:
            cube.doStrAct("U1" + "U5" + whereisedge)
            cube.doStrAct("U1" + "U5" + whereisedge)
            cube.doStrAct("U1" + "U5" + edge)

    for edge in ["D5", "D1"]:
        whereisedge = index2facelet[cube.data.index(edge)]
        if whereisedge in dedges:
            cube.doStrAct("U1" + "U5" + whereisedge)

        whereisedge = index2facelet[cube.data.index(edge)]
        cube.doStrAct("D1" + "D5" + whereisedge)

    for i in range(2):
        nowis = cube.data[facelet2index["U1"]]
        if nowis in twoedges:
            break
        cube.doStrAct("U1" + "U5" + "B1")
        
    

if __name__ == '__main__':
    case = ''.join([random.choice('UuDdLlRrFfBb') for i in range(random.randint(10, 30))])

    c = cube(e)
    print("====================     run       =========================")
    print("CASE:  ", len(case), case)
    for i in case:
        c.doStrAct(i, verbose=False)
    c.actionsList = []
    c.actionsList2 = []


    print("====================  corner =========================")
    print("before cube: ", corner_cube_perm(c))
    print("before face: ", corner_face_perm(c))
    phase1(c)
    print("after cube: ", corner_cube_perm(c))
    print("after face: ", corner_face_perm(c))
    print("action list:")
    cacts = c.getActs()
    print(cacts)

    print("====================  edge  =========================")
    #c = cube(e)
    #for i in case:
    #    c.doStrAct(i, verbose=False)
    c.actionsList = []
    c.actionsList2 = []
    print("before cube: ", edge_cube_perm(c))
    print("before face: ", edge_face_perm(c))
    phase2(c)
    print("after cube: ", edge_cube_perm(c))
    print("after face: ", edge_face_perm(c))
    print("action list:")
    eacts = c.getActs()
    print(eacts)
    print("====================  all   =========================")
    print(cacts + eacts)
