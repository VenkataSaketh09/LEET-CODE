class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
      mod=10**9+7
      s1={}
      def rec(substr):
        if substr not in s1:
          count=0
          for char in set(substr):
            left,right=substr.find(char),substr.rfind(char)
            if left==right:
              count+=1
            else:
              count+=2+rec(substr[left+1:right])
          s1[substr]=count
        return s1[substr]
      return rec(s)%mod

        