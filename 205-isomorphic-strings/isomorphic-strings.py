class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        if len(s)!=len(t):
            return 0
        for i in range(len(s)):
            chr1=s[i]
            chr2=t[i]

            if(chr1 in d1 and d1[chr1]!=chr2) or (chr2 in d2 and d2[chr2]!=chr1):
                return 0
            d1[chr1]=chr2
            d2[chr2]=chr1
        return 1
        