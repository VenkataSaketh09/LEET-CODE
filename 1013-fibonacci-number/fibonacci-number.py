class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0:
            return a
        elif n==1:
            return b
        else:
            return self.fib(n-1)+self.fib(n-2)
        