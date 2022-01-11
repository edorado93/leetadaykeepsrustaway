class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node, value):
            if not node:
                return 0
            
            value = (value << 1) + (1 if node.val else 0)
            recursion_answers = recurse(node.left, value) + recurse(node.right, value)
            
            if not node.left and not node.right:
                recursion_answers += value
                
            return recursion_answers
        
        return recurse(root, 0)
        
        
        
