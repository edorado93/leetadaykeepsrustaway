class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        @lru_cache(None)
        def palinPartition(index):
            
            if index == len(s):
                return [[]]
            
            sub = ""
            current_partitions = []
            for j in range(index, len(s)):
                sub += s[j]
                
                # It's a palindrome
                if sub == sub[::-1]:
                    partitions = palinPartition(j + 1)
                    
                    for p in partitions:
                        current_partitions.append([sub] + p)
                        
            return current_partitions
        
        return palinPartition(0)
        
