import typing

'''
Hash table
Implement a class that can instantiate a key-value storage object 
(the keys will be strings and the values will be integers); 
these objects should have similar semantics to a Ruby hash / Python dict / JS object. 
Its methods should include:
get
set
Ensure your object maintains performance even when a large number of key-values are added.
Assume we've implemented a hash function for you:
function hash(<string> key) {
    // Returns an integer between -4E9 and 4E9.
}
Note: Data should be stored in an array.
table = HashTable()
hashtable.set('a', 1)
hashtable.set('b', 2)
hashtable.get('a') // returns 1
hashtable.get('b') // returns 2

'''

class Bucket:
    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k,v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        found = False
        for idx, (k,v) in enumerate(self.bucket):
            if k == key:
                self.bucket[idx] = (key,value)
                found = True
        
        if not found:
            self.bucket.append((key,value))
            
    def remove(self, key):
        for idx, (k,v) in enumerate(self.bucket):
            if k == key:
                del self.bucket[idx]

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_space = 2069
        self.hash_table = [Bucket() for x in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bucket = self.hash_table[hash(key) % self.key_space]
        bucket.update(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket = self.hash_table[hash(key) % self.key_space]
        return bucket.get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket = self.hash_table[hash(key) % self.key_space]
        bucket.remove(key)





# class hashtable(object):
#     def __init__(self,capacity):
#         self.capacity = capacity
#         self.keys = []
#         self.vals = []
#         
#     def empty(self):
#         
#         if not self.keys:
#             return True
#         return False
# 
#     def hash_imp(self, key):
#         return hash(key) % self.capacity
#     
#     
#     def set(self, key:str, val:int):
#         
#         
#         index = self.hash_imp(key, val)
#         
#         
#         if not self.vals[index]:
#             self.vals[index] = []
#     
#         else:
#             items =  self.vals[index]
#             for i in range(len(items)): 
#                 # find will be fast
#                 if items[i][0] == key:
#                     items[i] = (key, val)
#                              
#                 self.vals[index].append((key,val))
#     
# 
#     def get(self, key:str):
#         index = self.hash_imp(key)
#         
#         items =  self.vals[index]
#         
#         for i in range(len(items)): 
#             # find will be fast
#             if items[i][0] == key:
#                 return items[i][1]
# 
#         return None
        
            
        