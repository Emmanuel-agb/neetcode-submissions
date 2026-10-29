class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):  # go through each row
            for j in range(len(matrix[0])):  # go through each column
                if matrix[i][j] == target:  # found target
                    return True  # return True
        return False  # checked all, not found
