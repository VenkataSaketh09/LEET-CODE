class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        sorted_strs=sorted(strs)
        first=sorted_strs[0]
        last=sorted_strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans


        