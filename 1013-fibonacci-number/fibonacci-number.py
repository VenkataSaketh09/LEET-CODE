class Solution:
    def fib(self, n: int) -> int:
        # a=0
        # b=1
        # if n==0:
        #     return a
        # elif n==1:
        #     return b
        # else:
        #     return self.fib(n-1)+self.fib(n-2)

        #Formula
        sqrt5=5**0.5
        val1=(1+sqrt5)
        val2=(1-sqrt5)
        ans=(val1/2)**n-(val2/2)**n
        return round(ans/sqrt5)
        