class Solution:
    
    def how_many_hours(self, piles, k):
        hours = 0
        for p in piles:
            hours += (p // k)
            hours += (p % k != 0)
        return hours
            
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        min_hours = float("inf")
        while l <= r:
            
            mid = (l + r) // 2
            hours_taken = self.how_many_hours(piles, mid)
            if hours_taken > h:
                l = mid + 1
            else:
                min_hours = min(min_hours, mid)
                r = mid - 1
                
        return min_hours
        
        
