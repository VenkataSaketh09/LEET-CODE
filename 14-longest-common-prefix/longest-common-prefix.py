class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==0:
          return ""
        if n==1:
          return strs[0]
        ind=0
        strs.sort()
        val=min(len(strs[0]),len(strs[-1]))
        while ind<val and strs[0][ind]==strs[-1][ind]:
          ind+=1
        if ind>=1:
          return strs[0][0:ind]
        else:
          return ""                  