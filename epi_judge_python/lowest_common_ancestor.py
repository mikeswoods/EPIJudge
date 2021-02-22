import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# Path approach:
# def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
#         node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

#     def compute_parents(node, prev, parents):
#       if node:
#         compute_parents(node.left, node, parents)
#         compute_parents(node.right, node, parents)
#         parents[node] = prev

#     def compute_path(node, parents):
#       path = []
#       it = node
#       while it:
#         path.insert(0, it)
#         it = parents[it]
#       return path

#     if not tree or not node0 or not node1:
#       return None

#     parents = {}
#     compute_parents(tree, None, parents)
#     node0_path = compute_path(node0, parents)
#     node1_path = compute_path(node1, parents)

#     lowest_ancestor = tree
#     while node0_path and node1_path:
#       n0 = node0_path.pop(0)
#       n1 = node1_path.pop(0)
#       if n0 == n1:
#         lowest_ancestor = n0

#     return lowest_ancestor


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

  def contains_node(tree, node):
    if not tree:
      return False
    if tree == node:
      return True
    if contains_node(tree.left, node):
      return True
    if contains_node(tree.right, node):
      return True
    return False

  def traverse(tree):
    if not tree:
      return tree

    node0_in_left = contains_node(tree.left, node0)
    node1_in_right = contains_node(tree.right, node1)
    if node0_in_left and node1_in_right:
      return tree

    node0_in_right = contains_node(tree.right, node0)
    node1_in_left = contains_node(tree.left, node1)

    if node0_in_right and node1_in_left:
      return tree

    if node0_in_left and node1_in_left:
      return traverse(tree.left)
    if node0_in_right and node1_in_right:
      return traverse(tree.right)

    # current root:
    return tree

  return traverse(tree)


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
