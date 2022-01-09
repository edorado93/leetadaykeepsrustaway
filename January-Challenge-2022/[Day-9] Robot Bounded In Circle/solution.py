class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        directions = {"N": (0, 1), "S": (0, -1), "E": (-1, 0), "W": (1, 0)}
        d_change_left = {"N": "W", "S": "E", "E": "N", "W": "S"}
        d_change_right = {"N": "E", "S": "W", "E": "S", "W": "N"}
        
        def simulate(p_x, p_y, d):
            for follow in instructions:
                if follow == "G":
                    incr = directions[d]
                    p_x += incr[0]
                    p_y += incr[1]
                elif follow == "L":
                    d = d_change_left[d]
                else:
                    d = d_change_right[d]
                    
            return p_x, p_y, d
        
        x, y, d = 0, 0, "N"
        m_x, m_y = -float("inf"), -float("inf")
        for _ in range(4):
            x, y, d = simulate(x, y, d)            
            m_x, m_y = max(abs(x), m_x), max(abs(y), m_y)
        
        x, y, d = simulate(x, y, d)
        return not (abs(x) > m_x or abs(y) > m_y)
            
