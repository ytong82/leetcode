from collections import Counter


class Solution:
    def threeSum(self, nums):
        l = len(nums)
        if l < 3:
            return []

        allzero = True
        for i in range(l):
            if nums[i] != 0:
                allzero = False

        if allzero:
            return [[0, 0, 0]]

        res = set()
        for i in range(l):
            tss = self.twoSum(nums[0:i] + nums[i+1:l], -nums[i])
            for ts in tss:
                if nums[i] < ts[0]:
                    res.add(tuple([nums[i], ts[0], ts[1]]))
                elif nums[i] > ts[1]:
                    res.add(tuple([ts[0], ts[1], nums[i]]))
                else:
                    res.add(tuple([ts[0], nums[i], ts[1]]))
        return res

    def twoSum(self, nums, target):
        book = dict(Counter(nums))
        l = len(nums)
        res = set()
        for i in range(l):
            other = target - nums[i]
            if other in book.keys():
                if nums[i] == other:
                    if book[nums[i]] >= 2:
                        res.add(tuple([nums[i], other]))
                else:
                    if nums[i] <= other:
                        res.add(tuple([nums[i], other]))
                    else:
                        res.add(tuple([other, nums[i]]))
        return res


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))