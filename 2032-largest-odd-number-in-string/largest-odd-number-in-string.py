class Solution:
    def largestOddNumber(self, num: str) -> str:
        return num[:max(num.rfind(x) for x in '13579')+1] 
        