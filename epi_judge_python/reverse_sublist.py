from typing import Optional

from list_node import ListNode
from test_framework import generic_test


L = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

def reverse(L: ListNode) -> ListNode:
  def reverse_rec(L, L_next):
    if L:
      print(f"<{L.data}, {L.next.data if L.next else '-'}>")
      reverse_rec(L.next, None if not L.next else L.next.next)
      if L_next:
        L_next.next = L
  reverse_rec(L, L.next)


reverse(L)
print(L)

# def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
#     # TODO - you fill in here.
#     return None


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('reverse_sublist.py',
#                                        'reverse_sublist.tsv', reverse_sublist))
