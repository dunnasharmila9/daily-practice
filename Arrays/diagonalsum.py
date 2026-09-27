# LeetCode 1572 - Matrix Diagonal Sum
# Return the sum of the elements on the primary and secondary diagonals.
class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        r=len(mat)
        sum=0
        for i in range(r):
            for j in range(r):
                if i+j==r-1 or i==j:
                    sum=sum+(mat[i][j])
        return sum            
