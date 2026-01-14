# 501. Find Mode in Binary Search Tree
# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently
# occurred element) in it.
# If the tree has more than one mode, return them in any order.
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:
# Input: root = [0]
# Output: [0]
# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due
# to recursion does not count).


# def findMode(self, root):
#    """
#    :type root: Optional[TreeNode]
#    :rtype: List[int]
#    """
#
#    # The first approach is just use a hashmap or a counter from collections and pop the most frequent elements
#    my_map = {}
#    def dfs(node):
#        if node is None:
#            return
#        if node.val not in my_map:
#            my_map[node.val] = 0
#        my_map[node.val] += 1
#        dfs(node.left)
#        dfs(node.right)
#    dfs(root)
#    return [key for key, value in my_map.items() if value == max(my_map.values())]


def findMode(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """

    # The second approach is to use a inorder traversal to get the most frequent element and his ocurrences
    # List of the most frequent elements
    modes = []
    # List of the max count and maximum value
    max_count_and_value_list = [0, 0]

    # Inorder traversal
    # the current count and value list is for keep track of the current count and value and compare with the maximum at
    # the moment
    def inorder(
        node,
        modes: list[int],
        max_count_and_value_list: list[int],
        current_count_and_value_list: list[int],
    ):
        if node is None:
            return
        inorder(
            node.left, modes, max_count_and_value_list, current_count_and_value_list
        )

        # Initialize the current count and value list
        if current_count_and_value_list[0] == 0:
            current_count_and_value_list[0] = 1
            current_count_and_value_list[1] = node.val
        # If the current value is the same as the current count and value list, increment the count
        elif node.val == current_count_and_value_list[1]:
            current_count_and_value_list[0] += 1
        # If the current value is not the same as the current count and value list, reset the count and value list
        else:
            current_count_and_value_list[0] = 1
            current_count_and_value_list[1] = node.val

        # If the current count is greater than the max count, update the max count and value list
        if current_count_and_value_list[0] > max_count_and_value_list[0]:
            max_count_and_value_list[0] = current_count_and_value_list[0]
            max_count_and_value_list[1] = current_count_and_value_list[1]

            # Clear the modes list and add the current value
            modes.clear()
            modes.append(current_count_and_value_list[1])
        # If the current count is equal to the max count, add the current value to the modes list
        elif current_count_and_value_list[0] == max_count_and_value_list[0]:
            modes.append(current_count_and_value_list[1])

        inorder(
            node.right, modes, max_count_and_value_list, current_count_and_value_list
        )

    inorder(root, modes, max_count_and_value_list, [0, 0])

    return modes
