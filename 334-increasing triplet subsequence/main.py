import math


class Solution:
    def increasingTriplet(self, nums):
        length = len(nums)
        if length < 3:
            return False
        mi = math.inf
        mi2 = math.inf

        for i in range(length):
            if nums[i] < mi:
                mi = nums[i]
            else:
                if nums[i] < mi2 and nums[i] != mi:
                    mi2 = nums[i]
                elif nums[i] > mi2:
                    return True
        return False


nums = [1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1]
nums3 = [3, 1, 4, 2, 5]
nums4 = [3, 1, 4, 2, 2]
nums5 = [1, 2]
nums6 = [1, 1, -2, 6]
solution = Solution()
print(solution.increasingTriplet(nums6))
