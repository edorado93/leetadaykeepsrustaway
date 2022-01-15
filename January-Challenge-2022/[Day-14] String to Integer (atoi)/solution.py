class Solution:
    
    def should_clamp_and_break(self, val, l_bound, r_bound):
        if val < 0 and val < l_bound:
                return True
        elif val > r_bound:
            return True
        
        return False
    
    def myAtoi(self, s: str) -> int:
        
        N = len(s)
        mul, i = 1, 0
        l_bound, r_bound = -(2 ** 31), ((2 ** 31) - 1)
        while i < N:
            
            c = s[i]
            
            # A sign
            if c == "-" or c == "+":
                mul *= (-1 if c == "-" else 1)
                i += 1
                break
            
            # A digit
            elif c.isdigit():
                break
            
            # If we encounter anything other than a whitespace, a digit, or a sign, we return
            elif c != " ":
                return 0
                
            i += 1
        
        # Edge case-1
        if i == N:
            return 0
        
        val = 0
        while i < N:
            c = s[i]
            
            if not c.isdigit():
                break
                
            val *= 10
            val += int(c)
            
            if self.should_clamp_and_break(val * mul, l_bound, r_bound):
                return l_bound if mul == -1 else r_bound
            
            i += 1
        
        return val * mul
            
                
        
            
