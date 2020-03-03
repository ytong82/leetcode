class Solution:
    def sortColors(self, nums):
        length = len(nums)
        if length == 0:
            return []

        counts = [0] * 3
        for i in range(length):
            counts[nums[i]] += 1

        for i in range(length):
            if i < counts[0]:
                nums[i] = 0
            elif i < counts[0] + counts[1]:
                nums[i] = 1
            else:
                nums[i] = 2


nums = [2, 0, 2, 1, 1, 0]
sol = Solution()
sol.sortColors(nums)
print(nums)
