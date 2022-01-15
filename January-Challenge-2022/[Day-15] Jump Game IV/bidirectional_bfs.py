from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        N = len(arr)
        
        if N <= 1:
            return 0
        
        common_vals = defaultdict(list)
        for idx, val in enumerate(arr):
            common_vals[val].append(idx)
        
        small_q = set([0])
        large_q = set([N - 1])
        next_q = set()
        small_level, large_level = 0, 0
        visited = {}
        
        while small_q:
            
            # pick the smaller queue
            if len(large_q) < len(small_q):
                small_q, large_q = large_q, small_q
                small_level, large_level = large_level, small_level
            
            for x in small_q:

                if arr[x] not in visited:
                    visited[arr[x]] = 1
                    for idx in common_vals[arr[x]]:
                        if idx != x:
                            
                            if idx in large_q:
                                return small_level + large_level + 1
                            
                            next_q.add(idx)

                if x > 0:
                    
                    if x - 1 in large_q:
                        return small_level + large_level + 1
                    
                    if arr[x - 1] not in visited:
                        next_q.add(x - 1)

                if x < N - 1:
                    
                    if x + 1 in large_q:
                        return small_level + large_level + 1
                    
                    if arr[x + 1] not in visited:
                        next_q.add(x + 1)
            
            small_q = next_q
            next_q = set()
            small_level += 1        
