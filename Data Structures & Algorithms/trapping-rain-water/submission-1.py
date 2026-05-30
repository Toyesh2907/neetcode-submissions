class Solution:
    def trap(self, height: List[int]) -> int:
        array_len = len(height)
        if array_len < 3:
            return 0

        left = 0
        right = array_len - 1 

        left_max = height[left]
        right_max = height[right]
        area = 0
        while(left < right):
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                area += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                area += right_max - height[right]
        return area