class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
      def finding(nums, expected, k):
            split_count = 1
            summ = 0
            for i in nums:
                if summ + i > expected:
                    summ = i  
                    split_count += 1
                else:
                    summ += i
            return split_count > k

      low = max(nums)
      high = sum(nums)
      while low < high:
        mid = (low + high) // 2
        if finding(nums, mid, k):
          low = mid + 1
        else:
          high = mid
      return low
        