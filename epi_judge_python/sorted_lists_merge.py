from typing import Optional, Tuple

from list_node import ListNode
from test_framework import generic_test


def take_head(L: ListNode) -> Tuple[ListNode, Optional[ListNode]]:
  tail = L.next
  L.next = None
  return (L, tail)


def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    if not L1:
      return L2
    if not L2:
      return L1

    head = tail = None

    while L1 and L2:
      if L1.data < L2.data:
        node, L1 = take_head(L1)
      else:
        node, L2 = take_head(L2)
      if not head:
        head = tail = node
      tail.next = node
      tail = node

    if L1:
      tail.next = L1
    if L2:
      tail.next = L2

    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
