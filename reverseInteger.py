class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        isNeg = False

        if x < 0:
            x *= -1
            isNeg = True
        while x > 0:
            res *= 10
            res += x%10
            x //= 10

        if isNeg:
            res *= -1
        LOWWERBOUND, UPPERBOUND = -2**31, 2**31-1
        if res < LOWWERBOUND or res > UPPERBOUND:
            return 0

        # print(res)
        return res

sol = Solution()
print(sol.reverse(-1534236469))