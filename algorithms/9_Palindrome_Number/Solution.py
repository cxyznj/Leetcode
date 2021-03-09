class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        halfrevert = 0
        while x > halfrevert:
            halfrevert = halfrevert * 10 + x % 10
            x = int(x / 10)
        return x == halfrevert or x == int(halfrevert / 10)
