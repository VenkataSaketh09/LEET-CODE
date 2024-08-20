class Solution:
    def minWindow(self, s: str, t: str) -> str:
      if not s or not t:
        return ""
      count=len(t)
      map=[0]*128
      left=0
      right=0
      min_len=float('inf')
      for char in t:
        map[ord(char)]+=1
      while right<len(s):
        if map[ord(s[right])]>0:
          count-=1
        map[ord(s[right])]-=1
        right+=1
        while count==0:
          if right-left<min_len:
            min_len=right-left
            ind=left
          map[ord(s[left])]+=1
          if map[ord(s[left])]>0:
            count+=1
          left+=1
      return "" if min_len==float('inf') else s[ind:ind+min_len]
        
          
        