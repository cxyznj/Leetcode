class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hash_table = dict()
        count = 0
        
        for a in A:
            for b in B:
                hash_table[a+b] = hash_table.get(a+b, 0) + 1
        
        for c in C:
            for d in D:
                count += hash_table.get(-(c+d), 0)
        
        return count
