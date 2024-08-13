class Solution:
    def calculating(self,val1,val2,oper):
      if oper=='+':
        return val1+val2
      elif oper=='-':
        return val1-val2
      elif oper=='*':
        return val1*val2
      else:
        return int(val1/val2)
    def evalRPN(self, tokens: List[str]) -> int:
      stack=[]
      for val in tokens:
        if len(val)==1 and ord(val)<48:
          int2=stack.pop()
          int1=stack.pop()
          operator=val
          ans=self.calculating(int1,int2,operator)
          stack.append(ans)
        else:
          stack.append(int(val))
      return stack.pop()
        