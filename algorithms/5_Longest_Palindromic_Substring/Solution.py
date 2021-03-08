class Solution:
    # manacher algorithm implement
    def longestPalindrome(self, s: str) -> str:
        s = self.modifyString(s)
        c = 0
        r = 0
        P = [0] * len(s)
        maxcenter = 0
        
        for i in range(len(s)):
            if i < r:
                mirror = 2 * c - i
                if mirror >= 0 and P[mirror] < r - i:
                    P[i] = P[mirror]
                    continue
                else:
                    P[i] = r - i
            
            a = i - (P[i] + 1)
            b = i + (P[i] + 1)
            while a >= 0 and b < len(s) and s[a] == s[b]:
                P[i] += 1
                a -= 1
                b += 1
            
            if b-1 > r:
                r = b-1
                c = i
                if P[maxcenter] < P[i]:
                    maxcenter = i
        
        return s[maxcenter-P[maxcenter]:maxcenter+P[maxcenter]+1].replace("#", "")
    
    def modifyString(self, s: str) -> str:
        mstr = ""
        for c in s:
            mstr += ("#" + c)
        mstr += "#"
        return mstr
