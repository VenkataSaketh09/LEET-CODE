class Solution:
    def largestOddNumber(self, num: str) -> str:
        # return num[:max(num.rfind(x) for x in '13579')+1] 
        n=len(num)
        result=n-1
        while result>=0 and int(num[result])%2==0:
            result-=1
        if result<0:
            return ""
        return num[:result+1]