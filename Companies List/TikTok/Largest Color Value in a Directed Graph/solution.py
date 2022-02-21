class Solution:
    
    def __init__(self):
        self.cycle_found = False
    
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        if not edges:
            return 1
        
        self.cycle_found = False
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            
        def dfs(node, frequencies, visited_colors):
            
            if self.cycle_found:
                return {}, -1
            
            if node in frequencies:
                return frequencies[node]

            # Mark the node as grey
            visited_colors[node] = 1
            
            max_freq = {}
            largest_value = 1
            
            if node in adj_list:
                for neighbor in adj_list[node]:
                    
                    if visited_colors.get(neighbor, 0) == 1:
                        self.cycle_found = True
                        return {}, -1

                    max_freq_neigh, largest_value_neigh = dfs(neighbor, frequencies, visited_colors)

                    largest_value = max(largest_value, largest_value_neigh)
                    for color in string.ascii_lowercase:
                        max_freq[color] = max(max_freq.get(color, 0), max_freq_neigh.get(color, 0))
                        largest_value = max(largest_value, max_freq[color])
            
            max_freq[colors[node]] = max_freq.get(colors[node], 0) + 1
            largest_value = max(largest_value, max_freq[colors[node]])
                
            frequencies[node] = max_freq, largest_value
            
            # Mark the node as black, meaning completed recursion
            visited_colors[node] = 2
            
            # print(node, frequencies[node])
            
            return frequencies[node]
        
        ans = 0
        frequencies, visited_colors = {}, {}
        for node in adj_list:
            ans = max(ans, dfs(node, frequencies, visited_colors)[1])
            if self.cycle_found:
                return -1
        return ans
