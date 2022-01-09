class Solution:
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])
        increments = [-1, 0, 1]
        
        dp = [[[0 for _ in range(m)] for _ in range(m)] for _ in range(n)]
        
        for row in range(n - 1, -1, -1):
            for col1 in range(m):
                for col2 in range(m):
                    
                    for i in range(3):
                        for j in range(3):
                            n_col1 = col1 + increments[i]
                            n_col2 = col2 + increments[j]
                    
                            if row == n - 1 or n_col1 < 0 or n_col2 < 0 or n_col1 == m or n_col2 == m:
                                continue
                            
                            dp[row][col1][col2] = max(dp[row][col1][col2], dp[row + 1][n_col1][n_col2])
            
                    dp[row][col1][col2] += (grid[row][col1] + grid[row][col2] if col1 != col2 else grid[row][col1])
                
        return dp[0][0][m - 1]
        
        
            
        
        
