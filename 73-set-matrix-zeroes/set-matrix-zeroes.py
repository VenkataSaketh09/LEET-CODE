class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        row_data=set()
        col_data=set()
        for i in range(rows):
          for j in range(cols):
            if matrix[i][j]==0:
              row_data.add(i)
              col_data.add(j)
        for i in row_data:
          for j in range(cols):
            matrix[i][j]=0
        
        for i in col_data:
          for j in range(rows):
            matrix[j][i]=0
        

        