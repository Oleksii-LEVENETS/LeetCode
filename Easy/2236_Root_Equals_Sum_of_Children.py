# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check_tree(self, root: Optional[TreeNode]) -> bool:
        return (root.val - root.left.val - root.right.val) == 0
