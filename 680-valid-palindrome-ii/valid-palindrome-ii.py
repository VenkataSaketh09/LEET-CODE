class Solution:
    def validPalindrome(self, s: str) -> bool:
        ptr1=0
        ptr2=len(s)-1
        while ptr1<=ptr2:
            if s[ptr1]!=s[ptr2]:
                st1=s[:ptr1]+s[ptr1+1:]
                st2=s[:ptr2]+s[ptr2+1:]
                return st1==st1[::-1] or st2==st2[::-1]
            ptr1+=1
            ptr2-=1
        return True

        