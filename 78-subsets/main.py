import copy


class Solution:
    def subsets(self, nums):
        if len(nums) == 0:
            return []

        def __doSubsets(nums, subset):
            if len(nums) == 0:
                res.append(subset)
                return

            __doSubsets(nums[1:], copy.deepcopy(subset))
            subset.append(nums[0])
            __doSubsets(nums[1:], copy.deepcopy(subset))

        res = []
        __doSubsets(nums, [])

        return res


nums = [1, 2, 3]
sol = Solution()
print(sol.subsets(nums))
