class Solution(object):
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def isSameTree(self, p, q):
        # Base case: If both trees are empty, they are considered the same.
        if not p and not q:
            return True

        # If one of the trees is empty or their values differ, they are not the same.
        if not p or not q or p.val != q.val:
            return False

        # Recursively check the left and right subtrees.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
