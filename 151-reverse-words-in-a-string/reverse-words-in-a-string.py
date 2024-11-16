class Solution:
    def reverseWords(self, s: str) -> str:
    #   data=s.split()
    #   return ' '.join(data[::-1])
        temp = ''
        ans = ''
        left = 0
        right = len(s) - 1

        while left <= right:
            char = s[left]
            if char != ' ':
                temp += char
            elif char == ' ':
                if temp:  # Ensure temp is not empty
                    if ans:
                        ans = temp + ' ' + ans
                    else:
                        ans = temp
                    temp = ''
            left += 1

        # Addinglast word to ans
        if temp:
            if ans:
                ans = temp + ' ' + ans
            else:
                ans = temp

        return ans
        