from model import *


def test(cases):
    for actions, result in cases:
        yield result == doStrActs(e, actions)
        

case1 = ("UUUUDDDDLLLLRRRRFFFFBBBB", e)

case2 = ("ULLFFFDRRBBB",
         ['B6', 'L5', 'L8', 'D3', 'U4', 'L3', 'B0', 'R3', 'F0', 'U8', 'U7', 'U0', 'D7', 'D4', 'U1', 'D2', 'D1', 'B8', 'D8', 'L7', 'U2', 'D5', 'L4', 'U5', 'R6', 'B7', 'R0', 'L2', 'B5', 'D0', 'R5', 'R4', 'U3', 'B2', 'B1', 'L6', 'R2', 'F5', 'U6', 'R1', 'F4', 'B3', 'F2', 'F1', 'L0', 'F6', 'F3', 'R8', 'L1', 'B4', 'R7', 'D6', 'F7', 'F8'])
         
case3 = ("FFLLBR",
         ['R2', 'R5', 'F6', 'D3', 'U4', 'F3', 'D6', 'D1', 'F0', 'U0', 'U7', 'F8', 'U3', 'D4', 'B7', 'R0', 'R3', 'B6', 'U2', 'L7', 'L6', 'U1', 'L4', 'L3', 'U8', 'L1', 'L0', 'L2', 'L5', 'L8', 'R7', 'R4', 'R1', 'D2', 'D7', 'D8', 'B8', 'F7', 'U6', 'B5', 'F4', 'D5', 'B2', 'F1', 'R6', 'D0', 'B3', 'B0', 'U5', 'B4', 'B1', 'R8', 'F5', 'F2'])

case4 = ("BBFRFU",
         ['D2', 'U3', 'D8', 'D1', 'U4', 'D7', 'D0', 'F1', 'F0', 'L0', 'R7', 'U8', 'D3', 'D4', 'B5', 'U2', 'U1', 'B8', 'F8', 'F7', 'F6', 'R5', 'L4', 'R3', 'R2', 'L7', 'B2', 'L2', 'B7', 'B6', 'L5', 'R4', 'R1', 'F2', 'L3', 'L6', 'L8', 'U7', 'U6', 'F5', 'F4', 'F3', 'U0', 'D5', 'R0', 'R8', 'L1', 'R6', 'U5', 'B4', 'B3', 'D6', 'B1', 'B0'])

case4 = ("UUULLDB",
         ['F2', 'R5', 'F8', 'D3', 'U4', 'U7', 'D6', 'U3', 'U6', 'U0', 'U1', 'U2', 'D7', 'D4', 'D1', 'L8', 'L5', 'B6', 'U8', 'L7', 'L6', 'U5', 'L4', 'L3', 'D0', 'B7', 'L0', 'F0', 'F1', 'D2', 'R3', 'R4', 'D5', 'R2', 'F7', 'D8', 'B8', 'L1', 'L2', 'B5', 'F4', 'F5', 'B2', 'B1', 'B0', 'R6', 'B3', 'R0', 'R7', 'B4', 'R1', 'R8', 'F3', 'F6'])

print(difference(case4[1], e))
d = [c1 == c2 for c1, c2 in zip(case4[1], e)]
for a, b, c in zip(e, d, case4[1]):
    print(a, b, c)


def main():
    print(list(test([case1, case2, case3, case4])))

if __name__ == '__main__':
    main()