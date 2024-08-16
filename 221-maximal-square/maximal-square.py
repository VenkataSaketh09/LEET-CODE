class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
      rows=len(matrix)
      cols=len(matrix[0])
      dp=[[0 for _ in range(cols+1)] for _ in range(rows+1)]
      for i in range(rows-1,-1,-1):
        for j in range(cols-1,-1,-1):
          if matrix[i][j]!='1':
            continue
          else:
            dp[i][j]=1+min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1])
      flatten_1D=sum(dp,[]) 
      return max(flatten_1D)**2
        