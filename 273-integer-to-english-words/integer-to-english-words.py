class Solution:
  def __init__(self):
    self.ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
    self.tens = ['', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
    self.thousands = ['', ' Thousand', ' Million', ' Billion']
  def converting(self,n:int)->str:
    if n<20:
      return self.ones[n]
    elif n<100:
      return self.tens[n//10]+self.converting(n%10)
    elif n<1000:
      return self.converting(n//100)+' Hundred'+self.converting(n%100)
    else:
      for i in range(3,0,-1):
        if n>=1000**i:
          return self.converting(n//(1000**i))+self.thousands[i]+self.converting(n%(1000**i))
    return ''
  def numberToWords(self, num: int) -> str:
    if num==0:
      return 'Zero'
    return self.converting(num).lstrip()

        