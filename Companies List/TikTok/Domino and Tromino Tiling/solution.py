class Solution:
    def numTilings(self, n: int) -> int:
        
        @lru_cache(None)
        def recurse(row, col, is_single):
            
            if col >= n:
                return col == n and not is_single
            
            ans = 0
            if is_single:
                domino = recurse(1 - row, col + 1, True)
                tromino = recurse(0, col + 2, False)
                ans = domino + tromino
            else:
                # |
                # |
                domino_one = recurse(0, col + 1, False)
                
                # __
                # __
                domino_two = recurse(0, col + 2, False)
                
                # |
                # |_
                tromino_one = recurse(0, col + 1, True)
                
                # |-
                # |
                tromino_two = recurse(1, col + 1, True)
                ans = domino_one + domino_two + tromino_one + tromino_two
                
            return ans % 1000000007
        
        return recurse(0, 0, False)
            
            
            
