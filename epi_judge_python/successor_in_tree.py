import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.

    root = node
    while root and root.parent:
      root = root.parent

    def walk(root):
      s = []
      current = root
      return_next = False
      while len(s) > 0 or current:
        if current:
          s.append(current)
          current = current.left
        else:
          if len(s) > 0:
            n = s.pop()
            if return_next:
              return n
            if n:
              if n == node:
                return_next = True
              current = n.right
      return None

    return walk(root)


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
