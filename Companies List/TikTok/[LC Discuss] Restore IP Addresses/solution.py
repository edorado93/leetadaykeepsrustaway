class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        def get_final_val(idx):
            val, j = 0, idx
            while j < len(s):
                val = (val * 10) + int(s[j])
                j += 1
                
            zero_validity = ((j - 1) == idx or s[idx] != '0')
            return val if ((val >= 0 and val <= 255) and zero_validity) else -1
    
        def backtrack(idx, dots_rem):
            
            if idx == len(s):
                return []
            elif dots_rem == 0:
                final_val = get_final_val(idx)
                return [] if final_val < 0 else [str(final_val)]
            
            valid_ips = []
            
            val = 0
            for j in range(idx, len(s)):
                
                val = (val * 10) + int(s[j])
                res = []
                
                zero_validity = (j == idx or s[idx] != '0')
                
                # We cannot consider the string [idx, j]. If we have
                # dots remaining, we should split
                if zero_validity and val >= 0 and val <= 255:
                    res = backtrack(j + 1, dots_rem - 1)
                    
                for ip in res:
                    valid_ips.append("{0}.{1}".format(val, ip))
                    
            return valid_ips
                    
        return backtrack(0, 3)       
                                    
        
