from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        book = dict(Counter(nums))

        res = []
        for key, value in sorted(book.items(), key=lambda item:item[1], reverse=True):
            res.append(key)
            k -= 1
            if k == 0:
                break
        return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))


