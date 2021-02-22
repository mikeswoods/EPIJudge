from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
  # def inorder_traversal_rec(tree, path):
  #   if tree:
  #     inorder_traversal_rec(tree.left, path)
  #     path.append(tree.data)
  #     inorder_traversal_rec(tree.right, path)

  # path = []
  # inorder_traversal_rec(tree, path)
  # return path

  s = []
  it = tree
  items = []

  while it or len(s) > 0:
    if it:
      s.append(it)
      it = it.left
    else:
      if len(s) > 0:
        it = s.pop()
        print(">", it.data)
        items.append(it.data)
        it = it.right

  return items


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
