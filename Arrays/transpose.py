# LeetCode 867 - Transpose Matrix
# Return the transpose of the given matrix by switching its rows and columns.
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m=len(matrix)
        n=len(matrix[0])
        result=[]
        for j in range(n): 
            row=[]
            for i in range(m):
                a=matrix[i][j]
                row.append(a)
            result.append(row)
        return result    
                
        