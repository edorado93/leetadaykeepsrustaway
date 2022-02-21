class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        adj_list = defaultdict(list)
        for u, v in dislikes:
            adj_list[u].append(v)
        
        def dfs(node, colors, curr_color):
            
            opp_color = curr_color + 1 if curr_color % 2 != 0 else curr_color - 1
            
            if node in adj_list:
                for neigh in adj_list[node]:
                    if neigh in colors:
                        if colors[neigh] == opp_color:
                            return False
                        continue
                    
                    colors[neigh] = curr_color
                    if not dfs(neigh, colors, opp_color):
                        return False
            return True
        
        colors = {}
        comp_color = 1
        for node in adj_list:
            if node not in colors:
                colors[node] = comp_color
                if not dfs(node, colors, comp_color):
                    return False
                comp_color += 2
        return True
                
        
            
            
        
