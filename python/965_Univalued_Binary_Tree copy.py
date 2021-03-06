# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isUnivalTree(self, root:TreeNode) -> bool:
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1
    

if __name__ == '__main__':
    # begin
    ar = [1,1,1,1,1,1,1]
    s = Solution()
    print (s.isUnivalTree(ar))
