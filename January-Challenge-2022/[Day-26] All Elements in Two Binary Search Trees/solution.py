
class Solution:
    
    def moveOneStep(self, stack):
        
        if not stack:
            return float("inf")
        
        node, op = stack.pop()
        
        # means we have not started processing this node's left subtree
        if op == 1:
            
            stack.append((node, 2))
            
            leftmost = node
            while leftmost.left:
                stack.append((leftmost.left, 2))
                leftmost = leftmost.left
                
            return self.moveOneStep(stack)
        
        # this implies we need to process the current node, and then add the right child
        else:
            
            # add the right node if available
            if node.right:
                stack.append((node.right, 1))
            return node.val
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        tree1_stack = [(root1, 1)] if root1 else []
        tree2_stack = [(root2, 1)] if root2 else []
        
        t1_val, t2_val = None, None
        output = []
        
        while tree1_stack or tree2_stack:
            
            if t1_val == None:
                t1_val = self.moveOneStep(tree1_stack)
                
            if t2_val == None:
                t2_val = self.moveOneStep(tree2_stack)
            
            if t1_val < t2_val:
                output.append(t1_val)
                t1_val = None
            else:
                output.append(t2_val)
                t2_val = None
        
        if t1_val and t1_val != float("inf"):
            output.append(t1_val)
        if t2_val and t2_val != float("inf"):
            output.append(t2_val)
        return output
