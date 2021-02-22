from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


total = 0
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
  def assign_parents(node, prev, parents):
    if node:
      assign_parents(node.left, node, parents)
      assign_parents(node.right, node, parents)
      assert node not in parents
      parents[node] = prev

  parents = {}
  assign_parents(tree, None, parents)

  def walk(tree):
    if not tree:
      return 0

    left_sum  = walk(tree.left)
    right_sum = walk(tree.right)
    center_sum = 0

    if not tree.left and not tree.right:
      it = tree
      path = []
      while it:
        path.insert(0, it.data)
        it = parents[it]
      center_sum = sum(x * (2 ** p) for x, p in enumerate(reversed(path)))

    return left_sum + center_sum + right_sum

  return walk(tree)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
