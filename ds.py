class Nd:
    def __init__(self, v):
        self.v = v
        self.nxt = None

class Stk:
    def __init__(self):
        self.tp = None
        self.sz = 0

    def psh(self, v):
        n = Nd(v)
        n.nxt = self.tp
        self.tp = n
        self.sz += 1

    def pp(self):
        if not self.tp: 
            return None
        v = self.tp.v
        self.tp = self.tp.nxt
        self.sz -= 1
        return v
        
    def is_emp(self):
        return self.sz == 0

class HNd:
    def __init__(self, u, p, s):
        self.u = u
        self.p = p
        self.s = s
        self.nxt = None

class HTbl:
    def __init__(self, cp=100):
        self.cp = cp
        self.arr = [None] * cp

    def _hsh(self, k):
        r = 0
        for c in k:
            r = (r * 31 + ord(c)) % self.cp
        return r

    def add_u(self, u, p, s=0):
        idx = self._hsh(u)
        cur = self.arr[idx]
        while cur:
            if cur.u == u: 
                return False
            cur = cur.nxt
        nn = HNd(u, p, s)
        nn.nxt = self.arr[idx]
        self.arr[idx] = nn
        return True

    def get_u(self, u):
        idx = self._hsh(u)
        cur = self.arr[idx]
        while cur:
            if cur.u == u: 
                return cur
            cur = cur.nxt
        return None
class QNd:
    def __init__(self, v):
        self.v = v
        self.nxt = None

class Qu:
    def __init__(self):
        self.hd = None
        self.tl = None

    def enq(self, v):
        n = QNd(v)
        if not self.tl:
            self.hd = self.tl = n
            return
        self.tl.nxt = n
        self.tl = n

    def deq(self):
        if not self.hd: 
            return None
        v = self.hd.v
        self.hd = self.hd.nxt
        if not self.hd: 
            self.tl = None
        return v
        
    def is_emp(self):
        return self.hd is None