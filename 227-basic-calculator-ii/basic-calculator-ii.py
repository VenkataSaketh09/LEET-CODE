class Solution:
    def calculate(self, s: str) -> int:
      val=0
      ope='+'
      stack=[]
      for i in s+'+':
        if i.isdigit():
          val=val*10+int(i)
        if i in '+/-*':
          if ope=='+':
            stack.append(val)
          elif ope=='-':
            stack.append(-val)
          elif ope=='*':
            stack.append(stack.pop()*val)
          else:
            stack.append(int(stack.pop()/val))
          ope=i
          val=0
      return sum(stack)
          

        