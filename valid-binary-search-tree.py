# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


def isValidBST(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """

    if root is None:
        return True

    def determine_validity(root, min=float("-inf"), max=float("inf")):
        if root is None:
            return True

        is_valid = min < root.val < max

        is_valid_left_subtree = True
        if root.left is not None:
            is_valid_left_subtree = determine_validity(root.left, min, root.val)

        is_valid_right_subtree = True
        if root.right is not None:
            is_valid_right_subtree = determine_validity(root.right, root.val, max)

        return is_valid and is_valid_left_subtree and is_valid_right_subtree

    return determine_validity(root)
