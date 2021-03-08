class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "": 
            return 0
        return self.KMP(haystack, needle)
        
    def KMP(self, text: str, pattern: str) -> int:
        nxt = [0] * len(pattern)
        self.getNext2(pattern, nxt)
        i = 0
        j = 0
        while i < len(text) and j < len(pattern):
            if j == -1 or text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = nxt[j]
        
        if j == len(pattern):
            return i - j
        else:
            return -1
        
        
    def getNext(self, pattern: str, nxt: List[int]):
        nxt[0] = -1
        i = 0
        j = -1
        while i < (len(pattern) - 1):
            if j == -1 or pattern[i] == pattern[j]:
                i += 1
                j += 1
                nxt[i] = j
            else:
                j = nxt[j]
                
