class Solution:
    def isValid(self, s: str) -> bool:
        di={'(':')','[':']','{':'}'}
        stack=[]
        for i in s:
            if i  in di:
                stack.append(i)
            else:
                if stack and di[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
        return not stack


        