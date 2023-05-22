class NodeTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    
    if root.val == p.val:
        return p
    elif root.val == q.val:
        return q
    
    if root.val < max(p.val, q.val) and root.val > min(p.val, q.val):
        return root
    
    return lowest_common_ancestor(root.left, p, q) or lowest_common_ancestor(root.right, p, q)