class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        # Find the maximum number of bits that can be set. This is the max we can achieve through XORing two
        # numbers together.
        maxBits = len(bin(max(nums))) - 2
        
        # Answer variable
        max_xor_prefix = 0
        
        # A mask of all ones from the left. This will help us expose prefixes. For example, the maxBits is 6 and say
        # we have a number 110101 and we want the first three bits. So, we AND this number with a mask of 111000 and we
        # get [110]000 which is the prefix we need. The last three bits would be the SAME for all the numbers due to the
        # mask and hence this works
        all_ones_mask = 0
        
        # Starting from the highest bit to the lowest bit
        for bit_to_set in range(maxBits - 1, -1, -1):
            
            # Simply adding that bit to the mask
            all_ones_mask |= (1 << bit_to_set)
            
            # Assume we can find a combination that sets this bit
            # e.g. bit_to_set = 4 and max_xor = 10000, then max_xor = 11000
            max_xor_prefix |= (1 << bit_to_set)
        
            # This is the hash-based two-sum approach. We check if max_xor_prefix ^ masked_num is
            # in our hash map. If it is, then it means some number, say Y ^ masked_num gives us the
            # max_xor_prefix which is what we want.
            pref_present = {}
            pair_found_for_prefix = False
            for n in nums:
                
                # Mask all but the first (maxBits - bit_to_set) bits
                masked_num = n & all_ones_mask
                
                if (max_xor_prefix ^ masked_num) in pref_present:
                    pair_found_for_prefix = True
                    break
                    
                pref_present[masked_num] = 1
                    
            # This bit cannot be set because there is no pair which forms this prefix.
            if not pair_found_for_prefix:
                max_xor_prefix ^= (1 << bit_to_set)
                    
        return max_xor_prefix
                    
                    
