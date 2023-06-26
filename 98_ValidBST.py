def valid_bst(root):

    def helper(node, l, r):
        if not node:
            return True
        if not (l < node.val and node.val < r):
            return False
        
        return (
            helper(node.left, l, node.val) and helper(node.right, node.val, r)
        )
    
    return helper(root, float('-inf'), float('inf'))