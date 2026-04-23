

class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
        

    def hash(self, key):
        return key % self.size 
   
   
    def put(self, key, value):
        index = self.hash(key)
        # table[5] = [(1,10), (2,20)]
        #put(2, 99)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key,value))

    def get(self, key):
        index = self.hash(key)
        for k ,v in self.table[index]:
            if k == key:
                return v
        return -1    

    def remove(self, key):
       index = self.hash(key)
       for i, (k, v) in enumerate(self.table[index]):
        if k == key:
            del self.table[index][i]
            return
    def print_Hash(self):
        for i ,table in enumerate(self.table): 
            if table:           
              print(i , "=>", table)  


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(2,99)
obj.put(1,70)

param_2 = obj.get(2)
print(param_2)
# obj.remove(1)
obj.print_Hash()