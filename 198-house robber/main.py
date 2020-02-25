class Solution:
    def rob(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        res = [0] * length
        for i in range(length):
            if i < 2:
                res[i] = nums[i]
            else:
                res[i] = max(res[i-1], max(res[:i-1]) + nums[i])
        return max(res)


nums = [1, 2, 3, 1]
nums2 = [2, 7, 9, 3, 1]
nums3 = [2, 1, 1, 2]
nums4 = []
nums5 = [2, 1]
solution = Solution()
print(solution.rob(nums5))