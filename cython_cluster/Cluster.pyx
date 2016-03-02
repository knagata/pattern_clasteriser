import Levenshtein as lv

class Genom:
    def __init__(self, item, id):
        self.item = item
        self.id = id
    
    def len(self):
        return len(self.items)
    
    def similarity(self, target):
        cdef float val = lv.distance(self.item,target.item)
        #print(self.id,target.id,val)
        return val

class Cluster:
    def __init__(self,item,id):
        self.genoms = []
        self.genoms.append(Genom(item,id))
    
    def similarity(self,target):
        cdef float sum = 0
        for a in self.genoms:
            for b in target.genoms:
                sum += a.similarity(b)
        sum /= len(self.genoms)+len(target.genoms)
        #print(sum*2)
        return sum*2
    
    def add(self,c):
        self.genoms.extend(c.genoms)