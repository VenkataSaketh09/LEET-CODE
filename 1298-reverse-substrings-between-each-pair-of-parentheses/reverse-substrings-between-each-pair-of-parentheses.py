class Solution:
    def reverseParentheses(self, s: str) -> str:
        s=list(s)
        stack=[]
        for i,ch in enumerate(s):
            if ch=='(':
                stack.append(i)
            elif ch==')':
                j=stack.pop()
                s[j:i]=s[i:j:-1]
        return ''.join(ch for ch in s if ch.isalpha())


        