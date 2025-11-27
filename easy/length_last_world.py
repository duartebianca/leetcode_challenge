class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        without_space = s.strip()
        reverse = without_space[::-1]
        last_word = []
        for c in reverse:
            if c == " ":
              return len(last_word)
            last_word.append(c)
        return len(last_word)