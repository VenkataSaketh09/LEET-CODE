class Solution:
    def reverse(self, x: int) -> int:
        num=abs(x)
        rev=0
        while num>0:
            dig=num%10
            rev=rev*10+dig
            num//=10
        if -2**31<=rev<=2**31-1:
            if x<0:
                return -rev
            else:
                return rev
        else:
            return 0
        