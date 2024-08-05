class Solution:
    def reverseWords(self, s: str) -> str:
      data=s.split()
      return ' '.join(data[::-1])
        