from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# [2]->[3]->[5]->[3]->[2]
# [5]->[3]->[2]->[2]->[3], k = 3
def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if k == 0 or not L:
      return L

    def length(L: ListNode) -> int:
      it = L
      n = 0
      while it:
        n += 1
        it = it.next
      return n

    def head_tail(L: ListNode) -> ListNode:
      head = tail = L
      before_tail = None
      while tail and tail.next:
        before_tail = tail
        tail = tail.next
      return head, tail, before_tail

    # k times:
    head = L
    n = length(L)
    k = k % n

    for _ in range(k):
      head, tail, before_tail = head_tail(head)
      tail.next = head
      before_tail.next = None
      head = tail
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
