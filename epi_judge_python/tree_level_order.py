from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
  if not tree:
    return []

  queue = [(0, tree)]
  depths = {}
  while len(queue) > 0:
    (depth, node) = queue.pop(0)

    if depth not in depths:
      depths[depth] = []

    depths[depth].append(node.data)

    if node.left:
      queue.append((depth + 1, node.left))
    if node.right:
      queue.append((depth + 1, node.right))

  return list(depths.values())


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
