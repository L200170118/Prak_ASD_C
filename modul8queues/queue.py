class Queue(object):    
    def __init__(self):
        self.qlist =[]
    def isEmpty(self):
        return len(self) == 0
    def __len__(self):
        return len(self.qlist)
    def enqueue(self, data):
        self.qlist.append(data)
    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist.pop(0)
    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[0]
    def getRearMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[-1]
        

q = Queue()
q.enqueue(67)
q.enqueue(43)
q.enqueue(89)

print (q.dequeue())
print (q.dequeue())

print (q.getFrontMost())
print (q.getRearMost())




