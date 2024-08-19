class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
      cur_sum=sum(cardPoints[:k])
      max_sum=cur_sum

      for i in range(1,k+1):
        sliding_sum=cardPoints[-i]-cardPoints[k-i]
        cur_sum+=sliding_sum
        max_sum=max(max_sum,cur_sum)
      return max_sum

        