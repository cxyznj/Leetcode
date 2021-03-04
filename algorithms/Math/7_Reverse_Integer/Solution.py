class Solution:
    def reverse(self, x: int) -> int:
        INF = 0x80000000 - 1
        res = 0
        symbol = 1
        if x < 0:
            symbol = -1
            x = -x
        while x > 0:
            print(x, res)
            pop = x % 10
            x = int(x / 10)
            if (symbol == 1 and res > int((INF - pop) / 10)) or (symbol == -1 and res > int((INF - pop + 1) / 10)):
                return 0
            res *= 10
            res += pop
        res *= symbol
        return res
