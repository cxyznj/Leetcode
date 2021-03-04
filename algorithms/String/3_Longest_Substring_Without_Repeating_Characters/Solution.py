class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        arr = []
        maxlen = 0
        for c in s:
            if c in pos:
                maxlen = (len(arr) if len(arr) > maxlen else maxlen)
                j = 0
                while arr[j] != c:
                    del pos[arr[j]]
                    j += 1
                del arr[:j+1]
                    
            pos[c] = len(arr)
            arr.append(c)
            
        return len(arr) if len(arr) > maxlen else maxlen
