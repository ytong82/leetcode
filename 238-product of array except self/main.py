class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        if not length > 1:
            return []
        product = 1
        zero_num = 0
        for i in range(length):
            if nums[i] != 0:
                product *= nums[i]
            else:
                zero_num += 1

        res = [0] * length
        if zero_num == 1:
            for i in range(length):
                if nums[i] == 0:
                    res[i] = product
        elif zero_num == 0:
            for i in range(length):
                res[i] = product // nums[i]
        return res


nums = [1, 2, 3, 4]
nums = [0, 0]
solution = Solution()
print(solution.productExceptSelf(nums))



