from typing import Optional, Tuple

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:

  def node_at(L: ListNode, index: int) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    prev = None
    current = L
    for _ in range(1, index):
      prev = current
      current = current.next
    return current, prev

  def reverse(L: ListNode) -> ListNode:
    def reverse_rec(prev, node, head):
      if not node:
        return head
      head = None
      if not node.next:
        head = node
      h = reverse_rec(node, node.next, head)
      if prev:
        prev.next = None
      node.next = prev
      return h

    return reverse_rec(None, L, None), L

  start_node, before_start_node = node_at(L, start)
  end_node, before_end_node = node_at(L, finish)
  after_end_node = end_node.next if end_node else None

  # Detach the [beginning:start node] sublist from the section to be sorted:
  if before_start_node:
    before_start_node.next = None

  # Detach the [end node:end] sublist from the section to be sorted:
  if end_node:
    end_node.next = None

  # Reverse the sublist [start node:end node]:
  reversed_head, reverse_tail = reverse(start_node)

  # Reattach:
  if before_start_node:
    before_start_node.next = reversed_head
  else:
    L = reversed_head

  # start_node is now the tail of the sub list:
  if reverse_tail:
    reverse_tail.next = after_end_node

  return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
