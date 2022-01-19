class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        left, right = None, None
        distance = 0
        for idx in range(len(seats)):
            if seats[idx]:
                left = right
                right = idx
                distance = max(distance, ((right - left) // 2 if left != None else idx))
        
        return max(distance, len(seats) - right - 1)
