class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            while res and res[-1] > nums[i] and len(res) + (len(nums) - i) > k:
                res.pop()
            res.append(nums[i])
        
        return res[:k]
