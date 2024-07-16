class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # return sqrt(num)==floor(sqrt(num))

        # for i in range(1,(num//2)+1):
        #     if i*i==num:
        #         return True
        #     elif i*i>num:
        #         return False

        left,right=1,(num//2)+1
        while left<=right:
            mid=(left+right)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                left=mid+1
            else:
                right=mid-1
        return False

        