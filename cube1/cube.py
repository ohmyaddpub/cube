import numpy as np

class cube():
    def __init__(self, data=[]):
        if not data:
            data = [[j + str(k) for k in range(i*3, i*3+3)] for j in "UDLRFB" for i in range(3)]
        self.data = np.array(data)
        self.u = self.data[0:3, 0:3]
        self.d = self.data[3:6, 0:3]
        self.l = self.data[6:9, 0:3]
        self.r = self.data[9:12, 0:3]
        self.f = self.data[12:15, 0:3]
        self.b = self.data[15:18, 0:3]
    
    def __eq__(self, other):
        return (self.data == other.data).all()

    def cycleFace(self, e1, e2, e3, e4):
        e1[1], e2[1], e3[1], e4[1] =  e4[1], e1[1], e2[1], e3[1]
        e1[0], e1[2], e3[0], e3[2] =  e3[2], e1[0], e1[2], e3[0]

    def cycleEdge(self, e1, e2, e3, e4):
        e1[0], e2[0], e3[0], e4[0] =  e4[0], e1[0], e2[0], e3[0]
        e1[1], e2[1], e3[1], e4[1] =  e4[1], e1[1], e2[1], e3[1]
        e1[2], e2[2], e3[2], e4[2] =  e4[2], e1[2], e2[2], e3[2]

    def U(self):
        self.cycleFace(self.u[0, :], self.u[:, 2], self.u[2, ::-1], self.u[::-1, 0])
        self.cycleEdge(self.f[0, :], self.l[0, :], self.b[0, :], self.r[0, :])

    def D(self):
        self.cycleFace(self.d[0, :], self.d[:, 2], self.d[2, ::-1], self.d[::-1, 0])
        self.cycleEdge(self.f[2, :], self.r[2, :], self.b[2, :], self.l[2, :])

    def L(self):
        self.cycleFace(self.l[0, :], self.l[:, 2], self.l[2, ::-1], self.l[::-1, 0])
        self.cycleEdge(self.f[:, 0], self.d[:, 0], self.b[::-1, 2], self.u[:, 0])

    def R(self):
        self.cycleFace(self.r[0, :], self.r[:, 2], self.r[2, ::-1], self.r[::-1, 0])
        self.cycleEdge(self.f[:, 2], self.u[:, 2], self.b[::-1, 0], self.d[:, 2])
    
    def F(self):
        self.cycleFace(self.f[0, :], self.f[:, 2], self.f[2, ::-1], self.f[::-1, 0])
        self.cycleEdge(self.u[2, :], self.r[:, 0], self.d[0, ::-1], self.l[::-1, 2])

    def B(self):
        self.cycleFace(self.b[0, :], self.b[:, 2], self.b[2, ::-1], self.b[::-1, 0])
        self.cycleEdge(self.u[0, :], self.l[::-1, 0], self.d[2, ::-1], self.r[:, 2])

    def run(self, actions):
        for action in actions:
            getattr(self, action)()
    
    def order(self, action):
        ndata = self.data.copy()
        for t in range(1, 1000):
            self.run(action)
            if (self.data == ndata).all():
                return t