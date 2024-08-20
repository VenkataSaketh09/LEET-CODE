class Solution:
    def nthUglyNumber(self, n: int) -> int:
      next_2=2
      next_3=3
      next_5=5
      i2,i3,i5=0,0,0
      ugly_num=[0]*n
      ugly_num[0]=1
      for i in range(1,n):
        next_ugly=min(next_2,next_3,next_5)
        ugly_num[i]=next_ugly
        if next_ugly==next_2:
          i2+=1
          next_2=ugly_num[i2]*2
        if next_ugly==next_3:
          i3+=1
          next_3=ugly_num[i3]*3
        if next_ugly==next_5:
          i5+=1
          next_5=ugly_num[i5]*5
      return ugly_num[-1]
        