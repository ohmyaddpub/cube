from model import *


def find(facelet, actionList):
    lastreach = {}
    reach = {facelet: ["e"]}

    while lastreach != reach:
        newks = reach.keys() - lastreach.keys()
        lastreach = reach.copy()
        for k in newks:
            actTok = reach[k]
            for act in actionList:
                newact = actTok + [act]
                newres = doStrActs(e, newact)
                newidx = newres.index(facelet)
                if newidx not in reach:
                    reach[newidx] = newact
    return reach


res = find(0, "UDLRFB")
for k, v in res.items():
    print(index2facelet[k], ''.join(v))