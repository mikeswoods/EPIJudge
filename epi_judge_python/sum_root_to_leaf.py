from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:

  def is_leaf(node):
    return node and not node.left and not node.right

  def walk(node, prev, parents):
    if node:
      parents[node] = prev
      if is_leaf(node):

      else:
        walk(node.left, node, parents)
        walk(node.right, node, parents)

  if not tree:
    return 0

  parents = {}
  walk(tree, None, parents)





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
