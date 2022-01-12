class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)
        
        itr, itr_parent = root, None
        while itr:
            itr_parent = itr
            if val < itr.val:
                itr = itr.left
            else:
                itr = itr.right
        
        if val < itr_parent.val:
            itr_parent.left = TreeNode(val)
        else:
            itr_parent.right = TreeNode(val)
            
        return root
            
