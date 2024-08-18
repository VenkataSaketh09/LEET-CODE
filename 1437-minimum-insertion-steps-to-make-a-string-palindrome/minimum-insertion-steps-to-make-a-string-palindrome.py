class Solution:
    def minInsertions(self, s: str) -> int:
      #the answer is len(s)-longest palindromic subsequence

      #longest palindromic subsequence
      if s==s[::-1]:
        return 0
      dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
      rev=s[::-1]
      n=len(s)
      for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
          if rev[i]==s[j]:
            dp[i][j]=1+(dp[i+1][j+1] if i+1<n and j+1<n else 0)
          else:
            dp[i][j]=max(dp[i+1][j] if i+1<n else 0,dp[i][j+1] if j+1<n else 0) 
      
      return n-dp[0][0]
        