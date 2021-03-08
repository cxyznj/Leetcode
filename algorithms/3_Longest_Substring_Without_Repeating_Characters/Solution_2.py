class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        maxlen = 0
        bg_idx = 0
        for i in range(len(s)):
            if s[i] in pos:
                maxlen = max(i - bg_idx, maxlen)
                bg_idx = max(bg_idx, pos[s[i]] + 1)
            pos[s[i]] = i
        return max(len(s) - bg_idx, maxlen)
