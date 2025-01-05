class Solution:
    def myAtoi(self, s: str) -> int:
        ans=0
        s=s.strip()
        if not s:
            return 0
        temp=1
        if s[0]=='-' or s[0]=='+':
            if s[0]=='-':
                temp=-1
            s=s[1:]
        for i in s:
            if not i.isdigit():
                break
            ans=ans*10+int(i)
        ans*=temp
        if ans<-2**31:
            return -2**31
        elif ans>2**31-1:
            return 2**31-1
        return ans


        