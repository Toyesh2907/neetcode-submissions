class Solution:
    def maxArea(self, heights: List[int]) -> int:
        array_len = len(heights)
        current_area = -1
        maximum_area = -1
        left = 0
        right = array_len - 1
        while(left < right):
            h_right = heights[right]
            h_left = heights[left]
            breadth = right - left
            current_area = min(h_right, h_left) * breadth
            maximum_area = max(current_area, maximum_area)
            if h_left >= h_right:
                right -= 1
            else:
                left += 1
        return maximum_area