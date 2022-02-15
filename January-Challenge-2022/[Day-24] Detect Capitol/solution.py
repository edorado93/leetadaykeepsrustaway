class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        upper = 0
        for c in word:
            if c.isupper():
                upper += 1
                
        return upper == len(word) or upper == 0 or (upper == 1 and word[0].isupper())
