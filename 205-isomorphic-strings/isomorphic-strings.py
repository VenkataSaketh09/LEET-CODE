class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        #for isomorphic we should check injective +surjective(one-one + onto mapping)
        di1={}
        di2={}
        for i in range(len(s)):
            chr1,chr2=s[i],t[i]
            if (chr1 in di1 and di1[chr1]!=chr2) or (chr2 in di2 and di2[chr2]!=chr1):
                return False
            di1[chr1]=chr2
            di2[chr2]=chr1
        return True