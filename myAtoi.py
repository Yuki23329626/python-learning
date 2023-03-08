class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        isNeg = 1
        leadingIsOver = False
        for i in range(len(s)):
            print(s[i])
            if s[i] == ' ':
                if leadingIsOver:
                    return res*isNeg
                continue
            if s[i] == '+':
                if leadingIsOver:
                    return res*isNeg
                leadingIsOver = True
                continue
            if s[i] == '-':
                if leadingIsOver:
                    return res*isNeg
                leadingIsOver = True
                isNeg = -1
                continue
            if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                 break
            leadingIsOver = True
            res *= 10
            res += ord(s[i])-ord('0')
        LOWWERBOUND, UPPERBOUND = -2**31, 2**31-1
        if res*isNeg < LOWWERBOUND:
            return LOWWERBOUND
        if res*isNeg > UPPERBOUND:
            return UPPERBOUND
        return res*isNeg
            

sol = Solution()
print(sol.myAtoi("0-4193-- with words"))