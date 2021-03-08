class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if (dividend == INT_MIN and divisor == -1):
            return INT_MAX
        sign = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        base = -1
        while dividend >= divisor:
            divisor <<= 1
            base += 1
            if dividend < divisor:
                divisor >>= 1
                dividend -= divisor
                divisor >>= base
                quotient += (1 << base)
                base = -1
        if sign:
            quotient = -quotient
        return quotient
