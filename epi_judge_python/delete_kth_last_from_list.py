from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
      return None

    first = second = L

    # Go to the k-th node:
    for _ in range(k):
      second = second.next

    # Now, move `first` and second by one position until `second` == tail(L).
    # When `second` == tail(L), `first` is the k-th last node.
    before_first = None
    while second:
      before_first = first
      first = first.next
      second = second.next

    if before_first:
      before_first.next = first.next
    else:
      # The node to delete, `first`, is the head of the list so skip it:
      L = first.next

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
