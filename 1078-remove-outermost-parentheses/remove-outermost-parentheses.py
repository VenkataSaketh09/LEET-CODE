class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=''
        count=0
        flag=True
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            elif s[i]==')':
                count-=1
            if count==1 and flag==True:
                flag=False
                continue
            if count==0 and flag==False:
                flag=True
                continue
            ans+=s[i]
        return ans 
        