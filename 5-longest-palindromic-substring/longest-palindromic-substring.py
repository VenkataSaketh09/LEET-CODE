class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=''
        maxi=0
        for i in range(len(s)):  #in every iterations two loops runs
            #for odd lengths
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>maxi:
                    maxi=r-l+1
                    ans=s[l:r+1]
                #expanding outwards
                l-=1
                r+=1
            #for evev lengths
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>maxi:
                    maxi=r-l+1
                    ans=s[l:r+1]
                #expnding outwards
                l-=1
                r+=1
        return ans
                
        