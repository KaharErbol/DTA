# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS approach
def levelOrder(root):
    res = []
    q = collections.deque()
    q.append(root)

    while q:
        q_len = len(q)
        level = []
        for i in range(q_len):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    
    return res

# DFS approach
def level_order(root):
    res = []
    if not root:
        return res
    
    def dfs(node, level):
        if len(res) == level:
            res.append([])
        res[level].append(node.val)

        if node.left:
            dfs(node.left, level+1)
        if node.right:
            dfs(node.right, level+1)

    dfs(root, 0)

    return res