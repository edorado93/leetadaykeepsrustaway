class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        sqrt_options = [x*x for x in range(1, int(n**0.5) + 1)]
        
        @lru_cache(None)
        def recurse(rem_n):
            
            # The opposite player wins because the current player can't make a move
            if rem_n == 0:
                return False
            
            for s in sqrt_options:
                
                if s > rem_n:
                    break
                
                if not recurse(rem_n - s):
                    return True
        
            return False
        
        return recurse(n)
