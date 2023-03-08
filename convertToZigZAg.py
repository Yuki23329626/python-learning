class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        str1 = [[] for i in range(numRows)]
        i = 0
        while i < len(s):
            loop = numRows*2-2
            if i%loop < numRows:
                # print(i%loop)
                str1[i%loop].append(s[i])
            else:
                # print(loop-i%loop)
                str1[loop-i%loop].append(s[i])
            i += 1
        for i in range(1,numRows):
            str1[0].extend(str1[i])
        return ''.join(str1[0])

sol = Solution()
print(sol.convert("PAYPALISHIRING",1))