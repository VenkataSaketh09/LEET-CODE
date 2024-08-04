class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
      dp=[[0]*(m+1) for _ in range(n+1)]
      for i in strs:
        val1,val2=i.count('1'),i.count('0')
        for i in range(n-val1,-1,-1):
          for j in range(m-val2,-1,-1):
            dp[i+val1][j+val2]=max(dp[i+val1][j+val2],dp[i][j]+1)
      return dp[-1][-1]

        