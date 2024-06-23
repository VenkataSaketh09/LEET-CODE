class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stck_arr=[-1]
        longest_length=0
        for i in range(len(s)):
            if s[i]=='(':
                stck_arr.append(i)
            else:
                stck_arr.pop()
                if not stck_arr:
                    stck_arr.append(i)
                else:
                    longest_length=max(longest_length,i-stck_arr[-1])
        return longest_length

        