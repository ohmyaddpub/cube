from cube import cube


def printall(*args):
    for i in zip(*args):
        print(*i)

def test(cases):
    for actions, result in cases:
        rc = cube(result)
        c = cube()
        c.run(actions)
        yield c == rc
        

case1 = ("UUUUDDDDLLLLRRRRFFFFBBBB",
         [['U0', 'U1', 'U2'], ['U3', 'U4', 'U5'], ['U6', 'U7', 'U8'], ['D0', 'D1', 'D2'], ['D3', 'D4', 'D5'], ['D6', 'D7', 'D8'], ['L0', 'L1', 'L2'], ['L3', 'L4', 'L5'], ['L6', 'L7', 'L8'], ['R0', 'R1', 'R2'], ['R3', 'R4', 'R5'], ['R6', 'R7', 'R8'], ['F0', 'F1', 'F2'], ['F3', 'F4', 'F5'], ['F6', 'F7', 'F8'], ['B0', 'B1', 'B2'], ['B3', 'B4', 'B5'], ['B6', 'B7', 'B8']])

case2 = ("ULLFFFDRRBBB",
         [['B6', 'L5', 'L8'], ['D3', 'U4', 'L3'], ['B0', 'R3', 'F0'], ['U8', 'U7', 'U0'], ['D7', 'D4', 'U1'], ['D2', 'D1', 'B8'], ['D8', 'L7', 'U2'], ['D5', 'L4', 'U5'], ['R6', 'B7', 'R0'], ['L2', 'B5', 'D0'], ['R5', 'R4', 'U3'], ['B2', 'B1', 'L6'], ['R2', 'F5', 'U6'], ['R1', 'F4', 'B3'], ['F2', 'F1', 'L0'], ['F6', 'F3', 'R8'], ['L1', 'B4', 'R7'], ['D6', 'F7', 'F8']])
         
case3 = ("FFLLBR",
         [['R2', 'R5', 'F6'], ['D3', 'U4', 'F3'], ['D6', 'D1', 'F0'], ['U0', 'U7', 'F8'], ['U3', 'D4', 'B7'], ['R0', 'R3', 'B6'], ['U2', 'L7', 'L6'], ['U1', 'L4', 'L3'], ['U8', 'L1', 'L0'], ['L2', 'L5', 'L8'], ['R7', 'R4', 'R1'], ['D2', 'D7', 'D8'], ['B8', 'F7', 'U6'], ['B5', 'F4', 'D5'], ['B2', 'F1', 'R6'], ['D0', 'B3', 'B0'], ['U5', 'B4', 'B1'], ['R8', 'F5', 'F2']])
         

def main():
    #print(list(test([case1, case2, case3])))
    c = cube()
    print(c.order("FR"))
    print(c.order("RFF"))

if __name__ == '__main__':
    main()