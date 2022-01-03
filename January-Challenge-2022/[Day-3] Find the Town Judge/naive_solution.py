class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trust_counter = {}
        cant_be_judge = set()
        for a, b in trust:
            trust_counter[b] = trust_counter.get(b, 0) + 1
            cant_be_judge.add(a)
        
        for person in range(1, n + 1):
            if trust_counter.get(person, 0) == n - 1 and person not in cant_be_judge:
                return person
        return -1
            
            
            
        
