class Solution:
    def romanToInt(self, s: str) -> int:
        data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}       
        ans=0
        for i in range(len(s)):
            if i+1<len(s) and data[s[i]]<data[s[i+1]]:
                ans-=data[s[i]]
            else:
                ans+=data[s[i]]
        return ans