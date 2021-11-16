import math


class Solution:
    def maxSumBST(self, root):

        self.maxsum = 0

        def helper(node):
            """dfs"""
            if node is None:
                return True, math.inf, -math.inf, 0

            if node.left is None and node.right is None:
                self.maxsum = max(self.maxsum, node.val)
                return True, node.val, node.val, node.val

            left_is_BST, left_min, left_max, sum_left = helper(node.left)
            right_is_BST, right_min, right_max, sum_right = helper(node.right)

            is_binary_search = left_is_BST and right_is_BST and right_min > node.val > left_max
            if is_binary_search:
                self.maxsum = max(self.maxsum, sum_left+sum_right+node.val)
            return (is_binary_search, min(node.val, left_min, right_min), max(node.val, left_max, right_max), node.val+sum_left+sum_right)

        helper(root)
        return self.maxsum
