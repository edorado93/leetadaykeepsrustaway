class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        
        prev = -1
        peak = None
        for i in range(len(arr)):
            
            curr = arr[i]
            
            if curr == prev:
                return False
            
            if peak and curr > prev:
                return False
            elif peak == None and curr < prev:
                peak = i - 1
        
            prev = curr
        return peak and peak > 0
        
