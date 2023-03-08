class Solution:
    def checkIfPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    def longestPalindrome(self, s: str) -> str:
        begin = 0
        length = len(s)
        while length >= 1:
            for begin in range(len(s)-length+1):
                # print("length:", length)
                b = self.checkIfPalindrome(s[begin:begin+length])
                if b:
                    # print(s[begin:begin+length])
                    return s[begin:begin+length]
            length -= 1

sol = Solution()

print(sol.longestPalindrome("d"))
# print(sol.longestPalindrome("addb"))