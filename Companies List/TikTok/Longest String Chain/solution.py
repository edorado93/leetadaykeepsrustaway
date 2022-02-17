class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        L = len(words)
        
        # Sort by the word's length
        words.sort(key=lambda x: len(x))
        
        # Create a set for faster searches
        words_dict = {words[i]: i for i in range(L)}
        
        dp = [1 for _ in range(L)]
        
        """
            O(NL^2)
        """
        
        # N
        for i in range(L):
            w = words[i]
            
            # L
            for j in range(len(w)):
                
                # L
                short_word = w[:j] + w[j+1:]
                if short_word in words_dict:
                    dp[i] = max(dp[i], dp[words_dict[short_word]] + 1)
        
        return max(dp)
                
                
