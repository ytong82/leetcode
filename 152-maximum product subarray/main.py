class Solution(object):
    def maxProduct(self, nums):
        length = len(nums)
        ma = [0] * length
        mi = [0] * length

        for index in range(length):
            if index == 0:
                ma[index] = nums[index]
                mi[index] = nums[index]
                res = nums[index]
            else:
                ma[index] = max(max(ma[index-1] * nums[index], mi[index-1] * nums[index]), nums[index])
                mi[index] = min(min(ma[index-1] * nums[index], mi[index-1] * nums[index]), nums[index])
                res = max(ma[index], res)
        return res


solution = Solution()
print(solution.maxProduct([2, -5, -2, -4, 3]))