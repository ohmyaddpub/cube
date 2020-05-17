import json
import itertools
import collections

from model import *
import utils


def calc():
    for i in range(1, 20):
        print(i)
        diffs = collections.Counter()
        for actions in itertools.product("UDLRFB", repeat=i):
            n = doStrActs(e, actions)
            diffs.update((difference(n, e),))
        with open("data2/%d.json" % i, "w") as d:
            json.dump(diffs, d)

def calc2():
    for i in range(9, 1000):
        print(i)
        diffs = collections.Counter()
        length = 6**(i - 6)
        count = 6**6

        product = itertools.product("UDLRFB", repeat=i)
        for _ in range(count):
            actions = next(product)
            ne = doStrActs(e, actions)
            diffs.update((difference(ne, e),))
            for _ in range(length - 1):
                next(product)
        with open("data2/%d.json" % i, "w") as d:
            json.dump(diffs, d)
    
def calc3():
    for i in range(1, 20):
        print(i)
        diffs = collections.Counter()
        for actions in itertools.product("UDLRFB", repeat=i):
            n = doStrActs(e, actions)
            diffs.update((differenceU(n, e),))
        with open("data3/%d.json" % i, "w") as d:
            json.dump(diffs, d)

def calc4():
    for i in range(1, 9):
        print(i)
        for actions in itertools.product("UuDdLlRrFfBb", repeat=i):
            n = doStrActs(e, actions)
            if differenceU(n, e) == 8:
                for i in range(9):
                    if n[i] != i:
                        print(index2facelet[i], index2facelet[n[i]] , ''.join(actions))

def calc42():
    res = {}
    for i in range(11, 15):
        print(i)
        for actions in itertools.product("BbUuDdRrFfLl", repeat=i):
            n = doStrActs(e, actions)
            if n[0] == "U0" and n[1] != "U1" and n[2] == "U2" and n[3] == "U3" and n[4] == "U4" and n[5] == "U5" and n[6] == "U6" and n[7] == "U7" and n[8] == "U8":
            # if n[9] == "D0" and n[10] != "D1" and n[11] == "D2" and n[12] == "D3" and n[13] == "D4" and n[14] == "D5" and n[15] == "D6" and n[16] == "D7" and n[17] == "D8":
                act = ''.join(actions)
                frm = n[1]
                if frm not in res:
                    res[frm] = act
                    print("new!", frm, act)
                    print(res, len(res))

def calc43():
    res = {}
    for i in range(1, 8):
        print(i)
        for actions in itertools.product("UuDdLlRrFfBb", repeat=i):
            n = doStrActs(e, actions)
            #if n[9] != 9 and n[10] == 10 and n[11] == 11 and n[12] == 12 and n[13] == 13 and n[14] == 14 and n[15] == 15 and n[16] == 16 and n[17] ==17:
            if n[0] != 0 and n[1] == 1 and n[2] == 2 and n[3] == 3 and n[4] == 4 and n[5] == 5 and n[6] == 6 and n[7] == 7 and n[8] == 8:
                act = ''.join(actions)
                frm = index2facelet[n[0]]
                if frm not in res:
                    res[frm] = act
                    print("new!", frm, act)
                    if len(res) == 14:
                        print(res)
                        break
                    

def calc5(ff, ft):
    df = facelet2index[ff]
    dt = facelet2index[ft]
    for i in range(1, 20):
        print(i)
        for actions in itertools.product("UuDdLlRrFfBb", repeat=i):
            n = doStrActs(e, actions)
            if n[dt] == df  and differenceU(n, e) == 8:
                print(''.join(actions))

if __name__ == "__main__":
    #calc5("U3", "L1")
    calc42()
