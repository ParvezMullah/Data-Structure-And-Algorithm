class Hashing:
    def __init__(self, arr):
        self.count = [0] * 256
        found_repeated = False
        for c in arr:
            if self.count[ord(c)] == 1:
                print('first repeated character is ', c)
                found_repeated = True
                break
            else:
                self.count[ord(c)] += 1
        if not found_repeated:
            print('No repeated character')

arr = ['a', 'b', 'c', 'a']
hashing = Hashing(arr)
        
