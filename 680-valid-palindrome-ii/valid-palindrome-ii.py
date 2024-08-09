class Solution:
    def validPalindrome(self, s: str) -> bool:
        ptr1=0
        ptr2=len(s)-1
        while ptr1<=ptr2:
          if s[ptr1]!=s[ptr2]:
            string1=s[:ptr1]+s[ptr1+1:]
            string2=s[:ptr2]+s[ptr2+1:]
            return (string1 == string1[::-1]) or (string2 == string2[::-1])
          ptr1+=1
          ptr2-=1
        return True
        