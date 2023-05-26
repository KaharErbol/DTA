def diameter(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)

        res[0] = max(res, left + right + 2)

        return 1 + max(left, right)
    
    dfs(root)

    return res[0]
