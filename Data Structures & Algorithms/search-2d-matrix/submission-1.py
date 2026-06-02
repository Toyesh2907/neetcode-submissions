class Solution:

    def binary_search(self, left: int, right: int, matrix: list[list[int]], target: int, col_len: int) -> bool:
        while(left <= right):
            middle = (left + right) // 2
            middle_elem = matrix[middle // col_len][middle % col_len]
            if middle_elem == target:
                return True
            elif middle_elem > target:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        return self.binary_search(left = 0, right = (rows * cols) - 1, matrix = matrix, target = target, col_len = cols)