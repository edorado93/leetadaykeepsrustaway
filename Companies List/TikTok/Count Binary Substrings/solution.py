class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        zeros, ones = 0, 0
        prev = None
    
        ans = 0
        for char in s:
            if not prev or prev == char or (zeros == 0 or ones == 0):
                zeros += (char == '0')
                ones += (char == '1')
            else:
                ans += min(zeros, ones)
                zeros = 1 if char == '0' else zeros
                ones = 1 if char == '1' else ones
                
            prev = char
        
        if zeros != 0 and ones != 0:
            ans += min(zeros, ones)
        
        return ans
