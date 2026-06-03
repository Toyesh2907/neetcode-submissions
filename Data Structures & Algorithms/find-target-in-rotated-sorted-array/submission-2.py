class Solution:

    def find_axis(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return l #left would be axis on which the array is rotated

    def binary_search(self, nums: list[int], target: int, left: int, right: int) -> int:
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        array_len = len(nums)
        axis = self.find_axis(nums = nums)
        
        left = 0
        right = array_len - 1
        if nums[axis] <= target <= nums[right]:
            return self.binary_search(nums = nums, target = target, left = axis, right = right)
        else:
            return self.binary_search(nums = nums, target = target, left = left, right = axis - 1)