class Solution:
    
    def maxCoins(self, nums: List[int]) -> int:
        
        # special case
        if len(nums) > 1 and len(set(nums)) == 1:
            return (nums[0] ** 3) * (len(nums) - 2) + nums[0] ** 2 + nums[0]
        
        nums = [1] + nums + [1]
        N = len(nums)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        
        # 0 .. N - 1 is the length of the nums with fake balloons at the end.
        for left in range(N - 2, 0, -1):
            for right in range(left, N - 1):
                for last_bll in range(left, right + 1):
                    coins = nums[left - 1] * nums[last_bll] * nums[right + 1]
                    remaining = dp[left][last_bll - 1] + dp[last_bll + 1][right]
                    dp[left][right] = max(dp[left][right], coins + remaining)
        
        return dp[1][N - 2]
    
