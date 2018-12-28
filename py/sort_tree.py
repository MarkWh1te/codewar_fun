# You are given a binary tree:
# class Node:
#     def __init__(self, L, R, n):
#         self.left = L
#         self.right = R
#         self.value = n
# Your task is to return the list with elements from tree sorted by levels,
#  which means the root element goes first,
#  then root children (from left to right) are second and third, and so on.

# Return empty list if root is None.

# Example 1 - following tree:

#                  2
#             8        9
#           1  3     4   5
# Should return following list:

# [2,8,9,1,3,4,5]
# Example 2 - following tree:

#                  1
#             8        4
#               3        5
#                          7
# Should return following list:

# [1,8,4,3,5,7]

# best practise

# from collections import deque

# def tree_by_levels(node):
#     if not node:
#         return []
#     res, queue = [], deque([
#         node,
#     ])
#     while queue:
#         n = queue.popleft()
#         res.append(n.value)
#         if n.left:
#             queue.append(n.left)
#         if n.right:
#             queue.append(n.right)
#     return res

from queue import Queue


def tree_by_levels(node):
    if not node:
        return []
    results = []
    first = Queue()
    second = Queue()
    first.put(node)
    while not first.empty():
        while not first.empty():
            node = first.get()
            results.append(node.value)
            if node.left:
                second.put(node.left)
            if node.right:
                second.put(node.right)
        first, second = second, first
    return results