class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        N, M = len(baseCosts), len(toppingCosts)
        
        def take_min(cost1, cost2):
            if abs(cost1) < abs(cost2):
                return True
            elif abs(cost1) == abs(cost2):
                return (target - cost1) < (target - cost2)
            else:
                return False
        
        @lru_cache(None)
        def recurse(curr_cost, quantity_one, quantity_two):
            
            # Let's see if we can beat this cost
            curr_min = target - curr_cost
            
            for i in range(M):
                
                potential_new_diff = target - (toppingCosts[i] + curr_cost)
                if abs(potential_new_diff) >= abs(target - curr_cost):
                    continue
                
                bit_check = (1 << i)
                cost = float("inf")
                
                # Both quantities are available for this topping
                if quantity_one & bit_check:
                    cost = recurse(curr_cost + toppingCosts[i], quantity_one ^ bit_check, quantity_two)
                
                # One quantity is available
                elif quantity_two & bit_check:
                    cost = recurse(curr_cost + toppingCosts[i], quantity_one, quantity_two ^ bit_check)
                
                if take_min(cost, curr_min):
                    curr_min = cost
            
            return curr_min
        
        nearest_cost = float("inf")
        for b in baseCosts:
            base_cost = recurse(b, (1 << M) - 1, (1 << M) - 1)
            if take_min(base_cost, nearest_cost):
                nearest_cost = base_cost
            
        return target - nearest_cost
