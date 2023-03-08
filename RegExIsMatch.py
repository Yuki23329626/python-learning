class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if i >= len(s) and j >= len(p): # both out of bounds, base case
                return True
            if j >= len(p): # p str have not matched
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == '.') # if true, i in bounds, and first char matches

            if (j+1) < len(p) and p[j+1] == "*": 
                if (j+3) < len(p) and p[j+3] == '*' and (p[j] == p[j+2] or p[j+2] == '.'):
                    return dfs(i, j+2)
                return dfs(i, j+2) or (match and dfs(i+1, j)) # use *, or dont use *

            if match:
                return dfs(i+1, j+1)
            return False # not * and no match
        return dfs(0, 0)

sol = Solution()
print(sol.isMatch('aaaaaaaaaaaaaaaaaaab', '.*a*.*a*.*a*.*a*.*a*.*a*.*v'))
# print(sol.isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*c'))
# print(sol.isMatch('a', 'ab*'))
# print(sol.isMatch('aab', 'c*a*b'))
# print(sol.isMatch('aab', 'c*a*b'))
# print(sol.isMatch('asdfgh', '.*fgh'))
# print(sol.isMatch('asdfgh', 'asd.*'))
# print(sol.isMatch('asdfgh', 'as.*gh'))
# print(sol.isMatch('asdfgh', '.*df.*'))
# print(sol.isMatch('aabbcc', 'a*b*c*'))
# print(sol.isMatch('aa', 'a.*a'))
# print(sol.isMatch('', '.*'))
