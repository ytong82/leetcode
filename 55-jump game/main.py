class Solution:
    def canJump(self, nums):
        length = len(nums)
        if length == 0:
            return True
        res = [False] * length

        for i in range(length):
            if i == 0:
                res[i] = True
            j = i - 1
            while j >= 0:
                if nums[j] >= i - j and res[j] == True:
                    res[i] = True
                    break
                j -= 1
        return res[-1]


nums = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

solution = Solution()
print(solution.canJump(nums2))

