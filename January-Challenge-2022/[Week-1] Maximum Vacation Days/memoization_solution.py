class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        
        N = len(days)
        K = len(days[0])
        
        @lru_cache(None)
        def letsHaveFun(current_city, weeks_rem):
            
            # base case
            if weeks_rem == 0:
                return 0
            
            current_week = K - weeks_rem
            
            # stay in the current city and play
            play_days = days[current_city][current_week]
            recursion_play_days = letsHaveFun(current_city, weeks_rem - 1)
            ans = play_days + recursion_play_days
            
            # decide to move to a different city
            for city in range(N):
                if city != current_city and flights[current_city][city]:
                    play_days = days[city][current_week]
                    recursion_play_days = letsHaveFun(city, weeks_rem - 1)
                    ans = max(ans, play_days + recursion_play_days)
                    
            return ans
        
        return letsHaveFun(0, K)
