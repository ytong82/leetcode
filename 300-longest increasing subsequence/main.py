class Solution:
    def lengthOfLIS(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        count = [1] * length

        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    count[i] = max(count[i], count[j] + 1)
        print(count)
        return max(count)


solution = Solution()
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 4]))
