# 257. Binary Tree Paths
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, return all root-to-leaf paths in any order.
#
# A leaf is a node with no children.
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:
#
# Input: root = [1]
# Output: ["1"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        res = []

        def backtrack(path, node):
            path.append(str(node.val))

            if node.left is None and node.right is None:
                print(path)
                str_path = "->".join(path)
                res.append(str_path)
                path.pop()
                print(path)
                return

            if node.left is not None:
                backtrack(path, node.left)

            if node.right is not None:
                backtrack(path, node.right)

            path.pop()

        backtrack([], root)

        return res


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
# def binaryTreePaths(self,root):
#    res = []
#
#    def backtrack(path, node):
#
#
#        if node.left is None and node.right is None:
#            res.append("->".join(path))
#            return
#
# Procesar hijo izquierdo:
#        if node.left is not None:
#            path.append(str(node.left.val))
#            backtrack(path, node.left)
#            path.pop()
#
# Procesar hijo derecho:
#        if node.right is not None:
#            path.append(str(node.right.val))
#            backtrack(path, node.right)
#            path.pop()
#
#    # Para el root, agregar su valor antes de empezar
#    backtrack([str(root.val)], root)
#    return res


def binaryTreePaths(root):
    if not root:
        return []

    res = []
    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()

        if not node.left and not node.right:
            res.append(path)

        if node.right:
            stack.append((node.right, path + "->" + str(node.right.val)))

        if node.left:
            stack.append((node.left, path + "->" + str(node.left.val)))

    return res
