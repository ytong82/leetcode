class Solution:
    def searchRange(self, nums, target):
        def doBinarySearch(nums, target, offset):
            length = len(nums)
            if length == 0:
                return [-1, -1]

            middle = length // 2
            if target == nums[middle]:
                # search left boundary
                left = middle - 1
                while left >= 0:
                    if target == nums[left]:
                        left -= 1
                    else:
                        break
                left += 1

                # search right boundary
                right = middle + 1
                while right < length:
                    if target == nums[right]:
                        right += 1
                    else:
                        break
                right -= 1

                return [offset+left, offset+right]

            elif target < nums[middle]:
                return doBinarySearch(nums[:middle], target, offset)
            elif target > nums[middle]:
                return doBinarySearch(nums[middle+1:], target, offset+middle+1)

        res = doBinarySearch(nums, target, 0)
        return res


nums = [5, 7, 7, 8, 8, 10]
target = 8

#nums = [1, 2, 3]
#target = 3

sol = Solution()
print(sol.searchRange(nums, target))
