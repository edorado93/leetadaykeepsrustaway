class Solution:
    def minTimeToType(self, word: str) -> int:
        
        ans = 0
        curr_char = 'a'
        for char in word:
            a = abs(ord(char) - ord(curr_char))
            b = 26 - a
            ans += min(a, b)
            curr_char = char
            
        return ans + len(word)
        
