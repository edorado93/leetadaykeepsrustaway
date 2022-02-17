class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        while tx > sx and ty > sy:
            if tx > ty:
                tx -= (ty * (tx // ty)) 
            else:
                ty -= (tx * (ty // tx))
        
        if tx < sx or ty < sy:
            return False
        elif tx == sx and ty == sy:
            return True
        elif tx == sx and ty > tx and (ty - sy) % sx == 0:
            return True
        elif ty == sy and tx > ty and (tx - sx) % sy == 0:
            return True
        return False
