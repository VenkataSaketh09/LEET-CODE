class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        res=[[-1 for x in range(cols)] for y in range(rows)]

        def inBound(i,j):
          return  (0<=i<rows) and (0<=j<cols)
        
        for i in range(rows):
          for j in range(cols):
            count=0
            for cord1,cord2 in [(i,j+1),(i,j-1),(i-1,j),(i+1,j),(i-1,j+1),(i+1,j-1),(i+1,j+1),(i-1,j-1)]:
              if inBound(cord1,cord2):
                count+=board[cord1][cord2]
            if count<2:
              res[i][j]=0
            elif board[i][j]==1 and (count==2 or count==3):
              res[i][j]=1
            elif board[i][j]==1 and count>3:
              res[i][j]=0
            elif board[i][j]==0 and count==3:
              res[i][j]=1
            else:
              res[i][j]=board[i][j]
        board[:]=res

              
        