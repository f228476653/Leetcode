class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root):
            if not root:return
            inorder(root.left)
            if self.prev_ is not None :self.min_val = min(self.min_val,root.val-self.prev_)
            self.prev_=root.val
            inorder(root.right)
        self.prev_=None
        self.min_val=float('inf')
        inorder(root)
        return self.min_val

class Solution1:
    def getMinimumDifference(self, root: TreeNode) -> int:
        output=[]
        self.inorder(root,output)
        minValue = float('inf')
        for i in range(len(output)-1):
            minValue= min(minValue, output[i+1]-output[i]) 
        return minValue

    def inorder(self,root,output):
        if root == None:
            return output
        else:
            self.inorder(root.left,output)
            print(output)
            output.append(root.val)
            print(output)
            self.inorder(root.right,output)
            print(output)

root = TreeNode(53)
root.left = TreeNode(22)
root.right = TreeNode(59)
root.right.left = TreeNode(57)
root.left.left = TreeNode(20)
root.left.right = TreeNode(30)

s = Solution1()
m = s.getMinimumDifference(root)