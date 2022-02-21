class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        s_freq = Counter(s)
        t_freq = Counter(t)
        
        ans = 0
        for char in s_freq:
            diff = t_freq.get(char, 0) - s_freq[char]
            if diff < 0:
                ans += -diff
                
        return ans
