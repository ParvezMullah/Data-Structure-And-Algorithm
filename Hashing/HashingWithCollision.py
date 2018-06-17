"""
hash function - modulo division (other options - folding, modified folding)
collision resolution - linear probe (other option 
                            - quadratic prob, open addressing, treem double hashing)

"""
class Hashing: 
    
    def __init__(self, initial_size):
        self.count = [None] * initial_size
        self.size = len(self.count)

    def put(self, value):
        index = value % self.size
        while self.count[index] != None:
            index = (index + 1) % self.size
        self.count[index] = value

    def get(self, key):
        index = key % self.size
        if self.count[index] == None:
            print(key, 'not present in hash table')
            return
        temp = index
        index = (index + 1) % self.size
        item_found = False
        while index != temp and self.count[index] != key:
            if self.count[index] == key:
                item_found = True
                break
            index = (index + 1) % self.size
        if item_found or self.count[index] == key:
            print(key, 'found at index', index)
        else:
            print(key, 'is not found', index, temp)

    def traverse(self):
        for index, value in enumerate(self.count):
            if value is not None:
                print(index, value)i55


arr = [1, 2, 3, 4]
hashing = Hashing(10)
hashing.put(10)
hashing.put(22)
hashing.put(32)
hashing.put(43)
hashing.get(43)
hashing.traverse()