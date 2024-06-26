class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set()
        for char in word:
            if char.upper() in word and char.lower() in word:
                s.add(char.lower())
        return len(s)
        