import numpy as np

class cube():
    def __init__(self):
        data = []
        data.extend([[j + str(k) for k in range(i*3+1, i*3+4)] for j in "UDLRFB" for i in range(3)])
        self.data = np.array(data)

        self.u = self.data[0:3, 0:3]
        self.d = self.data[3:6, 0:3]
        self.l = self.data[6:9, 0:3]
        self.r = self.data[9:12, 0:3]
        self.f = self.data[12:15, 0:3]
        self.b = self.data[15:18, 0:3]

        self.t = self.u.copy()
        self.initData = self.data.copy()

    def reset(self):
        self.data = self.initData.copy()
    
    def cycle(self, face):
        self.t[0] = face[0]
        face[0] = face[2]
        face[2] = self.t[0]
        face[:, :] = face.T[:, :]

    def U(self):
        self.cycle(self.u)
        self.t[0, :] = self.f[0, :]
        self.f[0, :] = self.r[0, :]
        self.r[0, :] = self.b[0, :]
        self.b[0, :] = self.l[0, :]
        self.l[0, :] = self.t[0, :]

    def D(self):
        self.cycle(self.d)
        self.t[2, :] = self.f[2, :]
        self.f[2, :] = self.l[2, :]
        self.l[2, :] = self.b[2, :]
        self.b[2, :] = self.r[2, :]
        self.r[2, :] = self.t[2, :]

    def L(self):
        self.cycle(self.l)
        self.t[:, 0] = self.f[:, 0]
        self.f[:, 0] = self.u[:, 0]
        self.u[:, 0] = self.b[:, 2]
        self.b[:, 2] = self.d[:, 0]
        self.d[:, 0] = self.t[:, 0]

    def R(self):
        self.cycle(self.r)
        self.t[:, 2] = self.f[:, 2]
        self.f[:, 2] = self.d[:, 2]
        self.d[:, 2] = self.b[:, 0]
        self.b[:, 0] = self.u[:, 2]
        self.u[:, 2] = self.t[:, 2]

    def F(self):
        self.cycle(self.f)
        self.t[2, :] = self.u[2, :]
        self.u[2, :] = self.l[::-1, 2]
        self.l[:, 2] = self.d[0, :]
        self.d[0, :] = self.r[::-1, 0]
        self.r[:, 0] = self.t[2, :]

    def B(self):
        self.cycle(self.b)
        self.t[0, :] = self.u[0, :]
        self.u[0, :] = self.r[:, 2]
        self.r[:, 2] = self.d[2, ::-1]
        self.d[2, :] = self.l[0, :]
        self.l[0, :] = self.t[0, :]

    def F2(self):
        # 2 6 8 4
        self.f[0, 1], self.f[1, 2], self.f[2, 1], self.f[1, 0] = \
        self.f[1, 0], self.f[0, 1], self.f[1, 2], self.f[2, 1]

        # 1 3 7 9
        self.f[0, 0], self.f[0, 2], self.f[2, 2], self.f[2, 0] = \
        self.f[2, 0], self.f[0, 0], self.f[0, 2], self.f[2, 2]

        self.u[2, 0], self.r[0, 0], self.d[0, 2], self.l[2, 2] = \
        self.l[2, 2], self.u[2, 0], self.r[0, 0], self.d[0, 2]

        self.u[2, 1], self.r[0, 1], self.d[0, 1], self.l[2, 1] = \
        self.l[2, 1], self.u[2, 1], self.r[0, 1], self.d[0, 1]

        self.u[2, 2], self.r[0, 2], self.d[0, 0], self.l[0, 2] = \
        self.l[0, 2], self.u[2, 2], self.r[0, 2], self.d[0, 0]