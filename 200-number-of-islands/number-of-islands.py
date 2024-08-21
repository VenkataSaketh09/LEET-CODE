class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      if not grid:
        return 0
      rows=len(grid)
      cols=len(grid[0])
      def dfs(i,j):
        if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!='1':
          return
        grid[i][j]='#' #to mark as visited
        dfs(i+1,j)
        dfs(i,j+1)
        dfs(i-1,j)
        dfs(i,j-1)
      islands=0
      for i in range(rows):
        for j in range(cols):
          if grid[i][j]=='1':
            dfs(i,j)
            islands+=1
      return islands
        