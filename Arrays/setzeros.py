# LeetCode 73 - Set Matrix Zeroes
# If an element is 0, set its entire row and column to 0.
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        rows=set()
        col=set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    rows.add(i)