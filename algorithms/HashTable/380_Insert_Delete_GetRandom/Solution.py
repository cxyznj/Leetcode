class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # this dictionary index the position of each data, the key is data, the value is the position(or the index)
        self.data_index = {}
        # this list store the inserted data
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # python use hashtable to implement dictionary, so the time costs of search a element in dictionary is O(1)
        if val in self.data_index:
            return False
        
        self.data_index[val] = len(self.data)
        # to append a element to a list in python is O(1) time complexity. To prove this, we need know how python implement list. When creating an list, python will allocate a certain amount of space to the list, assume the space is 8 elements. When the user attempt append the 9th element in the list, python will create a new list twice as much as the original, and copy the original list to the new one, then append the 9th element. In this case, assume N = 8, python will cost 2N+1 after append the 9th element(In details, N+1 times append elements, N times move a element to a new space). Therefore, the average time costs is O((2N+1)/N) = O(1).  
        self.data.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if not val in self.data_index:
            return False
        
        # exchage the element to be deleted with the end element and edit the index of data
        index_shouldbe_remove = self.data_index[val]
        self.data[index_shouldbe_remove] = self.data[-1]
        self.data_index[self.data[-1]] = index_shouldbe_remove
        # Simply, the deleted element does not need to be put to the end, just remove it with pop. Both operation cost O(1) time complexity.
        self.data_index.pop(val)
        self.data.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # Generate a random number cost O(1), because it based on a seed and a function that can generate a sequence.
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
