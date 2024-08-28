class Solution:
    def reorganizeString(self, s: str) -> str:
      di={}
      for char in s:
        di[char]=di.get(char,0)+1
      sorted_chars=sorted(di.keys(),key=lambda x:di[x],reverse=True)

      ans=[None]*len(s)

      if di[sorted_chars[0]]>(len(s)+1)//2:
        return ""

      pos=0
      for char in sorted_chars:
        for _ in range(di[char]):
          if pos>=len(s):
            pos=1
          ans[pos]=char
          pos+=2
      return ''.join(ans)


        