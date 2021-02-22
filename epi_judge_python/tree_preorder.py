from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
    s = [tree]
    items = []
    while len(s) > 0:
      n = s.pop()
      if n:
        items.append(n.data)
        if n.right:
          s.append(n.right)
        if n.left:
          s.append(n.left)
    return items


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_preorder.py', 'tree_preorder.tsv',
                                       preorder_traversal))
