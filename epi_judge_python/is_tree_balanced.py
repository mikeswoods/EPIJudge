from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
  def traverse(tree: BinaryTreeNode, depth: int) -> bool:
      if not tree:
        return (True, depth)

      (left_balanced, left_height) = traverse(tree.left, depth + 1)
      if not left_balanced:
        return (False, None)

      (right_balanced, right_height) = traverse(tree.right, depth + 1)
      if not right_balanced:
        return (False, None)

      balanced = abs(left_height - right_height) <= 1
      height = max(left_height, right_height)

      return (balanced, height)

  (balanced, _) = traverse(tree, 0)
  return balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
