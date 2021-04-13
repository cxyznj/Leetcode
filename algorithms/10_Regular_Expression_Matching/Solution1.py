class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None] * (len(p) + 1)] * (len(s) + 1)
        def dodp(i, j):
            if i > len(s) or j > len(p):
                return False
            if not dp[i][j]:
                if j == len(p):
                    dp[i][j] = (True if i == len(s) else False)
                else:
                    firstmatch = i < len(s) and p[j] in {s[i], '.'}
                    if j < len(p) - 1 and p[j+1] == '*':
                        dp[i][j] = (firstmatch and dodp(i+1,j)) or dodp(i, j+2)
                    else:
                        dp[i][j] = (firstmatch and dodp(i+1, j+1))
                    
            return dp[i][j]
        
        return dodp(0, 0)
