class Solution:
    
    def find_next_if_picked(self, endTime, idx, sortedTimes):
        
        l, r = idx, len(sortedTimes) - 1
        while l <= r:
            
            mid = l + ((r - l) // 2)
            
            # We found an entry whose start time is more or equal than the passed endTime
            if sortedTimes[mid][0] >= endTime:
                r = mid - 1
            else:
                l = mid + 1
                
        return r + 1 if r > idx else idx + 1
    
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        times = [(startTime[idx], endTime[idx], profit[idx]) for idx in range(len(startTime))]
        times.sort()
        
        N = len(startTime)
        
        @lru_cache(None)
        def recurse(idx):
            
            if idx >= N:
                return 0
            
            dont_pick = recurse(idx + 1)
            
            next_idx = self.find_next_if_picked(times[idx][1], idx, times)
            pick = recurse(next_idx) + times[idx][2]
            
            return max(dont_pick, pick)
        
        return recurse(0)
        
        
