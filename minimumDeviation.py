class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        temp1 = list(set(nums))
        _min = 10**9
        for i in range(len(temp1)):
            if temp1[i] % 2 == 0:
                _min = min(_min, temp1[i])
            else:
                _min = min(_min, temp1[i]*2)
        
        print("min:", _min)
        
        isloop = False
        while max(temp1) % 2 == 0 and not isloop:
            if max(temp1)//2 >= _min:
                temp1[temp1.index(max(temp1))] //= 2
                print("2:",temp1)
                continue
            isloop = True

        return abs(max(temp1) - _min)
        
sol = Solution()
print(sol.minimumDeviation([5,7,8]))