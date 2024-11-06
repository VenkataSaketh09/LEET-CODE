class Solution:
    def reverse(self, x: int) -> int:
        # if x>=0:
        #     ans=int(str(x)[::-1])
        # else:
        #     ans=int('-'+str(abs(x))[::-1])
        # return ans if  -2**31<=ans<=(2**31)-1 else 0
        temp=abs(x)
        rev=0
        while temp!=0:
            digit=temp%10
            rev=rev*10+digit
            temp//=10
        if -2**31<=rev<=2**31-1:
            if x<0:
                return -rev
            return rev
        return 0

        
        