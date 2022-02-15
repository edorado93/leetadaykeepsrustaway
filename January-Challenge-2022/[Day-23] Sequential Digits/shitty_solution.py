class Solution:
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        digs = len(str(low))
        ans = []
        val = int("".join([str(i) for i in range(1, digs + 1)]))
        add = int("".join(str(1) for i in range(1, digs + 1)))
        itr = 9 - digs + 1
        
        while val <= high:
            
            if val >= low:
                ans.append(val)
            
            val += add
            itr -= 1
            
            # Increase digits and restart
            if itr == 0:
                digs += 1
                val = int("".join([str(i) for i in range(1, digs + 1)]))
                add = int("".join(str(1) for i in range(1, digs + 1)))
                itr = 9 - digs + 1
                
        return ans
