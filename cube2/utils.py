import model


model.registerActs("UUU", name='u')
model.registerActs("DDD", name='d')
model.registerActs("LLL", name='l')
model.registerActs("RRR", name='r')
model.registerActs("FFF", name='f')
model.registerActs("BBB", name='b')


d0corner = {'R0': 'lUL', 'L2': 'luL', 'F0': 'FUf', 'B2': 'Fuf', 'B0': 'UlUL', 'F2': 'UluL', 'L0': 'uFUf', 'R2': 'uFuf', 'F6': 'lULFUf', 'U2': 'luLFUf', 'U6': 'lfLLFL', 'U8': 'lflFuL', 'L8': 'FufluL', 'U0': 'FLFlUf'}
for frm, r1 in d0corner.items():
    r3 = ''.join([i.lower() if i.isupper() else i.upper() for i in r1[::-1]])
    r2 = "D"; r4 = "d"
    model.registerActs(''.join([r1, r2, r3, r4]), name="D0" + "D6" + frm)
    r2 = "d"; r4 = "D"
    model.registerActs(''.join([r1, r2, r3, r4]), name="D0" + "D2" + frm)
    r2 = "DD"; r4 = "DD"
    model.registerActs(''.join([r1, r2, r3, r4]), name="D0" + "D8" + frm)


u0corner = {'R8': 'lDL', 'L6': 'ldL', 'B8': 'BDb', 'F6': 'Bdb', 'F8': 'DlDL', 'B6': 'DldL', 'L8': 'dBDb', 'R6': 'dBdb', 'B2': 'lDLBDb', 'D2': 'ldLBDb', 'D6': 'lfDDFL', 'D8': 'lfdFdL', 'L0': 'BdbldL', 'D0': 'BLBlDb'}
for frm, r1 in u0corner.items():
    r3 = ''.join([i.lower() if i.isupper() else i.upper() for i in r1[::-1]])
    r2 = "U"; r4 = "u"
    model.registerActs(''.join([r1, r2, r3, r4]), name="U0" + "U6" + frm)
    r2 = "u"; r4 = "U"
    model.registerActs(''.join([r1, r2, r3, r4]), name="U0" + "U2" + frm)
    r2 = "UU"; r4 = "UU"
    model.registerActs(''.join([r1, r2, r3, r4]), name="U0" + "U8" + frm)


u1edge = {'L3': 'URuDb', 'R7': 'UruDB', 'L7': 'uLUdb', 'R5': 'ulUdB', 'B7': 'BUdru', 'F3': 'BuDlU', 'F5': 'bUdRu', 'F7': 'UDruDB', 'D7': 'LrBBlR', 'B3': 'UUFuDru', 'B5': 'UUfUdLU', 'L5': 'UrUdFUU', 'R3': 'uLuDfUU', 'D5': 'DLrBBlR', 'D3': 'dLrBBlR', 'D1': 'URfrFruB', "B1": "BUdRRUUDDLU"}
for frm, r1 in u1edge.items():
    r3 = ''.join([i.lower() if i.isupper() else i.upper() for i in r1[::-1]])
    r2 = "U"; r4 = "u"
    model.registerActs(''.join([r1, r2, r3, r4]), name="U1" + "U3" + frm)
    r2 = "u"; r4 = "U"
    model.registerActs(''.join([r1, r2, r3, r4]), name="U1" + "U5" + frm)
    r2 = "UU"; r4 = "UU"
    model.registerActs(''.join([r1, r2, r3, r4]), name="U1" + "U7" + frm)


d1edge = {'B5': 'FUdlD', 'F1': 'FuDrd', 'B3': 'fuDRd', 'L5': 'DRUdf', 'R1': 'DrUdF', 'L1': 'dLuDf', 'R3': 'dluDF', 'B1': 'UDrUdF', 'U7': 'LrFFlR', 'U5': 'FUfurfR', 'U3': 'fuFULFl', 'F5': 'DDBUdrd', 'F3': 'DDbuDLD', 'L3': 'DruDBDD', 'R5': 'dLUdbDD', 'U1': 'FUlULfuf'}
for frm, r1 in d1edge.items():
    r3 = ''.join([i.lower() if i.isupper() else i.upper() for i in r1[::-1]])
    r2 = "D"; r4 = "d"
    model.registerActs(''.join([r1, r2, r3, r4]), name="D1" + "D3" + frm)
    r2 = "d"; r4 = "D"
    model.registerActs(''.join([r1, r2, r3, r4]), name="D1" + "D5" + frm)
    r2 = "DD"; r4 = "DD"
    model.registerActs(''.join([r1, r2, r3, r4]), name="D1" + "D7" + frm)