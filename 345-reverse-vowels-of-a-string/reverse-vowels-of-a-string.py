class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels='aeiouAEIOU'
        left=0
        right=len(s)-1
        data=list(s)
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
                continue
            while left<right and s[right] not in vowels:
                right-=1
                continue
            data[left],data[right]=data[right],data[left]
            left+=1
            right-=1
        return ''.join(data)

