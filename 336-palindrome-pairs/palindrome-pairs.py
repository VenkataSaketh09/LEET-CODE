class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
      di={word:index for index,word in enumerate(words)}
      ans=[]
      for index,word in enumerate(words):
        for j in range(len(word)+1):
          left_word=word[:j]
          left_rev=left_word[::-1]
          right_word=word[j:]
          right_rev=right_word[::-1]

          if left_rev in di and di[left_rev]!=index and right_word==right_rev:
            ans.append([index,di[left_rev]])
          #it is complementary to the above logic
          if j>0 and right_rev in di and di[right_rev]!=index and left_word==left_rev:
            ans.append([di[right_rev],index])
      return ans

        