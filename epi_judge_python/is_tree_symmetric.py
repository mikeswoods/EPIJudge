from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
  def compare_trees(t1: BinaryTreeNode, t2: BinaryTreeNode) -> bool:
    if not t1 and not t2:
      return True
    if t1 and t2:
      return t1.data == t2.data and compare_trees(t1.left, t2.right) and compare_trees(t1.right, t2.left)
    return False

  if not tree:
    return True
  return compare_trees(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
