class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # Sort by start time
        points.sort()
        
        arrows = 1
        l, r = points[0]
        
        for p_l, p_r in points:
            
            # Need a new arrow at this point
            if p_l > r:
                arrows += 1
                l, r = p_l, p_r
            else:
                l = max(l, p_l)
                r = min(r, p_r)
        
        return arrows
        
