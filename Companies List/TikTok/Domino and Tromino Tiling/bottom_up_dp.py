class Solution:
    def numTilings(self, n: int) -> int:
        
        dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n + 3)]
        for col in range(n, -1, -1):
            for row in range(2):
                for is_single in range(2):
                    
                    if col == n and not is_single:
                        dp[col][row][is_single] = 1
                        continue
                    
                    if is_single:
                        domino = dp[col + 1][1 - row][1]
                        tromino = dp[col + 2][0][0]
                        dp[col][row][is_single] = domino + tromino
                    else:
                        domino_one = dp[col + 1][0][0]
                        domino_two = dp[col + 2][0][0]
                        tromino_one = dp[col + 1][0][1]
                        tromino_two = dp[col + 1][1][1]
                        dp[col][row][is_single] = domino_one + domino_two + tromino_one + tromino_two
                        
                    dp[col][row][is_single] %= 1000000007
                    
        return dp[0][0][0]
            
            
            
