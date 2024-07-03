class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        slider=0
        for i in range(min(3,len(arr))):
            slider+=arr[i]%2
        if slider==3:
            return True
        for i in range(3,len(arr)):
            slider+=arr[i]%2
            slider-=arr[i-3]%2
            if slider==3:
                return True
        return False
        