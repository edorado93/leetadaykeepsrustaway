class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        m, n = len(rooms), len(rooms[0])
        INF = 2147483647
        
        gates_q = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates_q.append((i, j))
        
        directions = [1, -1]
        
        level = 0
        while gates_q:
            
            sz = len(gates_q)
            for _ in range(sz):
                g_i, g_j = gates_q.popleft()
                for dx in directions:
                    g_dx_i = g_i + dx
                    g_dx_j = g_j + dx
                    
                    if g_dx_j >= 0 and g_dx_j < n and rooms[g_i][g_dx_j] == INF:
                        rooms[g_i][g_dx_j] = level + 1
                        gates_q.append((g_i, g_dx_j))
                    if g_dx_i >= 0 and g_dx_i < m and rooms[g_dx_i][g_j] == INF:
                        rooms[g_dx_i][g_j] = level + 1
                        gates_q.append((g_dx_i, g_j))
                    
            level += 1
            
            
