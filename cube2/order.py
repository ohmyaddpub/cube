from model import *
import itertools



def order(actions):
    now = e
    for i in range(10000):
        nxt = doStrActs(now, actions)
        if nxt == e:
            return i
    else:
        return 0



def calc1():
    orders = set()
    for actions in itertools.product("UDLRFB", repeat=8):
        orders.add(order(actions))
    print(orders)

calc1()
        