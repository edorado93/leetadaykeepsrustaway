class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_w = s.split(" ")
        
        if len(s_w) != len(pattern):
            return False
        
        words, characters = {}, {}
        for idx in range(len(pattern)):
            char = pattern[idx]
            word = s_w[idx]
            
            if word in words and char in characters and words[word] != char and characters[char] != word:
                return False
            elif word in words and char not in characters:
                return False
            elif word not in words and char in characters:
                return False
            
            words[word] = char
            characters[char] = word
            
        return True
            
