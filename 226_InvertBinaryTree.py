class TreeNode:
    def __init__(self,left=None, right=None, val=0):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val} -left-> {self.left} -right-> {self.right}"

def invertTree(root):
    if not root:
        return root
    
    old_left = root.left
    root.left = invertTree(root.right)
    root.right = invertTree(old_left)

    return root

root = TreeNode(val=1, left=TreeNode(val=2,left=TreeNode(val=3),right=TreeNode(val=4)), right=TreeNode(val=5,left=TreeNode(val=6),right=TreeNode(val=7)))
print(root)
print(invertTree(root))