from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
  def get_height(root: BinaryTreeNode) -> int:
    if not root:
      return 0
    return max(1 + get_height(root.left), 1 + get_height(root.right))

  if not tree:
    return True

  print(tree)

  return abs(get_height(tree.left) - get_height(tree.right)) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
