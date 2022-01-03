import math
class Solution:
    
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        counter_mod = {}
        ans = 0
        for val in time:
            
            mod = val % 60
            
            if mod == 0:
                ans += counter_mod.get(0, 0)
            if (60 - mod) in counter_mod:
                ans += counter_mod[60 - mod]
                
            counter_mod[mod] = counter_mod.get(mod, 0) + 1
                
        return ans
                
