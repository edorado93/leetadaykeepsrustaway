class Solution:
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        increments = [-1, 0, 1]
        
        @lru_cache(None)
        def recurse(row, col1, col2):
            
            if row == n or col1 < 0 or col2 < 0 or col1 == m or col2 == m:
                return 0

            rec_ans = 0
            for i in range(3):
                for j in range(3):
                    n_col1 = col1 + increments[i]
                    n_col2 = col2 + increments[j]
                    rec_ans = max(rec_ans, recurse(row + 1, n_col1, n_col2)) 
                    
            return rec_ans + (grid[row][col1] + grid[row][col2] if col1 != col2 else grid[row][col1])
        
        return recurse(0, 0, m - 1)
        
            
        
        
