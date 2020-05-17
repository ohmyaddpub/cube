import random
import itertools
from cube import cube

def fuzzOrder():
    c = cube()

    orders = set([])
    acts = {}
    for length in range(7):
        for actions in itertools.product("UDLRFB", repeat=length):
            actions = "".join(actions)
            order = c.order(actions)
            orders.add(order)
            res = fun(order)
            acts[res] = actions
    print(acts)
    return orders

def fun(num):
    res = ""
    if not isinstance(num,int) or num <0:
        print("it is not a correct number")
    elif num==1:
        return "1"
    else:
        while num != 1:
            for i in range (2,num+1):
                if num%i==0:
                    num=int(num/i)
                    if num==1:
                        res += "%d" % i
                    else:
                        res += "%d*" % i
                    break
    return res

if __name__ == "__main__":
    c = cube()
    orders = fuzzOrder()
    #print(c.order("BBRFFD"))