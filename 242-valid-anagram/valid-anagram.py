class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s=sorted(s)
        # t=sorted(t)
        # return s==t
        data=[0]*26
        for i in s:
            data[ord(i)-ord('a')]+=1
        for i in t:
            data[ord(i)-ord('a')]-=1
        for i in range(26):
            if data[i]!=0:
                return False
        return True
        