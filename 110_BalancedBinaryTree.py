def is_balanced(root):
    def depth(root):
        if root is None:
            return 0

        left = depth(root.left)
        if left == -1:
            return -1
        
        right = depth(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1
    
    return True if depth(root) != -1 else False