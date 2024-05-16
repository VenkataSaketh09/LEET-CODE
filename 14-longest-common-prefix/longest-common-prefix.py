class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        if n==0:
            return ""
        elif n==1:
            return strs[0]
        else:
            strs.sort()
            i=0
            value=min(len(strs[0]),len(strs[n-1]))
            while i<value and strs[0][i]==strs[len(strs)-1][i]:
                i+=1
            if i>=1:
                return strs[0][0:i]
            else:
                return ""
        