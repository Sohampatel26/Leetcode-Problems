class Solution:
    def longestWord(self, words: List[str]) -> str:
        valid = set([""])
        for word in sorted(words, key=len):
            if word[:-1] in valid:
                valid.add(word)
        return max(sorted(valid), key=len) 