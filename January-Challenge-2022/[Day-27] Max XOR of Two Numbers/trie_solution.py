class Trie:
    
    def __init__(self, max_bits):
        self.root = {}
        self.max_bits = max_bits - 1
        
    def add(self, number):
        
        curr_node = self.root
        curr_bit = (1 << self.max_bits)
        while curr_bit:
            bit = 1 if curr_bit & number else 0
            curr_node[bit] = curr_node.get(bit, {})
            curr_node = curr_node[bit]
            curr_bit >>= 1
        
        curr_node["val"] = number
        
    
    def find_max_xor_number(self, number):
        
        curr_node = self.root
        curr_bit = (1 << self.max_bits)
        while curr_bit:
            opp_bit = 0 if curr_bit & number else 1
            
            # Best case is to find the opposite bit at this position
            if opp_bit in curr_node:
                curr_node = curr_node[opp_bit]
            else:
                # If we can't find that opposite bit, we go with the other bit. No other option
                curr_node = curr_node[1 - opp_bit]
            curr_bit >>= 1
                
        return curr_node["val"]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        trie = Trie(len(bin(max(nums))) - 2)
        for n in nums:
            trie.add(n)
            
        max_xor = 0
        for n in nums:
            
            # For the number "n" find the number which will give the maximum XOR value
            max_xor_number = trie.find_max_xor_number(n)
            max_xor = max(max_xor, n ^ max_xor_number)
        
        return max_xor
                    
                    
