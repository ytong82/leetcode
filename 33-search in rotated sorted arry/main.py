class Solution:
    def search(self, nums, target):
        length = len(nums)
        if length == 0:
            return -1
        elif length == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        def findPeakElement(nums, left, right):
            if nums[0] <= nums[-1]:
                return length - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > nums[mid+1]:
                    return mid
                elif nums[left] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def binarySearch(nums, target, left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if target == nums[mid]:
                    return mid
                elif target <= nums[mid]:
                    right = mid - 1
                    return binarySearch(nums, target, left, right)
                else:
                    left = mid + 1
                    return binarySearch(nums, target, left, right)
            return -1

        peak = findPeakElement(nums, 0, length-1)
        if peak == -1:
            return -1
        if target == nums[peak]:
            return peak
        if target > nums[peak]:
            return -1
        if peak == length - 1:
            if target < nums[0]:
                return -1
        elif target < nums[peak+1]:
            return -1

        if target > nums[0]:
            return binarySearch(nums, target, 0, peak-1)
        elif target < nums[0]:
            return binarySearch(nums, target, peak+1, length-1)
        else:
            return 0


nums = [4, 5, 1, 2, 3]
target = 1
sol = Solution()
print(sol.search(nums, target))
