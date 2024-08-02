class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
      def finding(string):
              stack=[]
              for char in string:
                if char=='#':
                  if stack:
                    stack.pop()
                else:
                  stack.append(char)
              return stack
      return finding(s)==finding(t)      

      
        