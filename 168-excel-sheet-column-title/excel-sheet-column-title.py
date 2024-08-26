class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
      ans=[]
      while columnNumber:
        columnNumber,remainder=divmod(columnNumber-1,26)
        ans.append(chr(65+remainder))
      return ''.join(ans[::-1])

        