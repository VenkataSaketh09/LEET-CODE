class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        for i in t:
            if d.get(i,0)==0:
                return False
            d[i]-=1
        return True
        