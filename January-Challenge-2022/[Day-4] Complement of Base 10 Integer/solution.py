class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        bits_needed = 0
        org_n = n
        while n > 0:
            bits_needed += 1
            n = n >> 1
        
        all_ones = (1 << bits_needed) - 1
        return all_ones ^ org_n
        
        
