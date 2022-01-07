class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        start_time = sorted(trips, key=lambda x: x[1])
        end_time = sorted(trips, key=lambda x: x[2])
        
        s, e, n = 0, 0, len(trips)
        
        max_passengers = -1
        curr_passengers = 0
        while s < n and e < n:
            
            if end_time[e][2] <= start_time[s][1]:
                curr_passengers -= end_time[e][0]
                e += 1
            else:
                curr_passengers += start_time[s][0]
                s += 1
            
            max_passengers = max(max_passengers, curr_passengers)
            
        return max_passengers <= capacity
            
            
