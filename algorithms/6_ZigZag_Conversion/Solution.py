class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Consider z is consisit of two base parts, and one oblique part
        res = ""
        n = len(s)
        # The interval of every adjacent base part is 2*numRows - 2
        # Specifically, 2*numRows - 2 = numRows:base interval + numRows - 2:oblique interval
        base = max(2*numRows - 2, 1)
        for i in range(numRows):
            idx = i
            while idx < n:
                res += s[idx]
                # For non-first and last rows, have one char in oblique part between every two base parts.
                # base - 2 * i can also be calculate(easy)
                if (i > 0) and (i < numRows - 1) and (idx+base-2*i < n):
                        res += s[idx+base-2*i]
                idx += base
        return res
