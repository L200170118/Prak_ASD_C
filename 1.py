class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self)==0

    def __len__(self):
        return len(self.items)

    def peek(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa diintip"
        return self.items[-1]

    def pop(self):
        assert not self.isEmpty(), "Stack kosong. Tidak bisa di-pop"
        return self.items.pop()

    def push(self, data):
        self.items.append(data)
        

def cetakHexa(d):
    f = Stack()
    if d == 0: f.push(0);
    while d != 0:
        if d%16 == 10:
            sisa = 'A'
        elif d%16 == 11:
            sisa = 'B'
        elif d%16 == 12:
            sisa = 'C'
        elif d%16 == 13:
            sisa = 'D'
        elif d%16 == 14:
            sisa = 'E'
        elif d%16 == 15:
            sisa = 'F'
        else:
            sisa = d%16
        d = d//16
        f.push(sisa)
    st = ""
    for i in range (len(f)):
      st = st + str(f.pop())
    return st
