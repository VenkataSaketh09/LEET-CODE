class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            curr_temp=temperatures[i]
            while stack and curr_temp>=temperatures[stack[-1]]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]-i  #distance
            stack.append(i)
        return ans
        