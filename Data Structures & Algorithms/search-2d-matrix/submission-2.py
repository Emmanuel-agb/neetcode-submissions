class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])  # size of matrix
        left, right = 0, rows * cols - 1  # search range as 1D

        while left <= right:  # binary search
            mid = (left + right) // 2  # middle index
            mid_val = matrix[mid // cols][mid % cols]  # convert to row, col

            if mid_val == target:  # found target
                return True  # return True
            elif mid_val < target:  # middle too small
                left = mid + 1  # search right half
            else:  # middle too big
                right = mid - 1  # search left half

        return False  # not found
