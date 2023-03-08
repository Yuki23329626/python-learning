class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        if temp < 0:
            return False
        rev = 0
        while temp > 0:
            rev *= 10
            rev += temp%10
            temp //= 10
        return True if rev == x else False

sol = Solution()
print(sol.isPalindrome(121))