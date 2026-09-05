class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1 = str(x)
        f = x1[::-1] == x1
        return f
        