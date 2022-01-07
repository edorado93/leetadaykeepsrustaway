class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        passenger_track = [0 for _ in range(1001)]
        for p, s, e in trips:
            passenger_track[s] += p
            passenger_track[e] -= p
            
        curr_passengers = 0
        for val in passenger_track:
            curr_passengers += val
            
            if curr_passengers > capacity:
                return False
            
        return True
        
            
            
