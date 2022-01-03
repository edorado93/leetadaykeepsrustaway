class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trust_counter = [0 for i in range(n)]
        for a, b in trust:
            trust_counter[a - 1] = -float("inf")
            trust_counter[b - 1] += 1
            
        negs = 0
        candidate = None
        for i in range(n):
            negs += trust_counter[i] == -float("inf")
            if trust_counter[i] == n - 1:
                candidate = i + 1
                
        return -1 if negs != n - 1 or candidate == None else candidate
            
            
        
