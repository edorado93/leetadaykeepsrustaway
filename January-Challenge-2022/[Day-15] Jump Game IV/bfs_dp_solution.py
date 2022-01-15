from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        N = len(arr)
        common_vals = defaultdict(list)
        for idx, val in enumerate(arr):
            common_vals[val].append(idx)
        
        q = deque([N - 1])
        min_jumps = {N - 1: 0}
        visited = {}
        
        while q:
            x = q.popleft()
            
            if arr[x] not in visited:
                visited[arr[x]] = 1
                for idx in common_vals[arr[x]]:
                    if idx != x:
                        q.append(idx)
                        min_jumps[idx] = min(min_jumps.get(idx, N), min_jumps[x] + 1)
                    
            if x > 0 and arr[x - 1] not in visited:
                q.append(x - 1)
                min_jumps[x - 1] = min(min_jumps.get(x - 1, N), min_jumps[x] + 1)
            
            if x < N - 1 and arr[x + 1] not in visited:
                q.append(x + 1)
                min_jumps[x + 1] = min(min_jumps.get(x + 1, N), min_jumps[x] + 1)
          
        return min_jumps[0]
                
        
        
